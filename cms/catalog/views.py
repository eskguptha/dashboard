from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import FormView, View
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render_to_response, render, redirect, HttpResponseRedirect, get_list_or_404, get_object_or_404
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import string
import random
from django.db.models import Q
from .models import *
from django.template.defaultfilters import removetags
from django.db.models import Sum
import datetime
from django.db import connection
import json


# Create your views here.

def randon_string_generator(stype, size):
    if stype == 'char':
        chars = string.ascii_uppercase + string.ascii_lowercase + ','
    elif stype == 'string':
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + ','
    elif stype == 'number':
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def dashboard(request, template_name="catalog/dashboard.html"):
    y,m,d = (datetime.datetime.now().strftime('%Y-%m-%d')).split('-')
    start = "%s-%s-01"%(y,07)
    end = datetime.datetime.now().strftime('%Y-%m-%d')
    dates = start+' - '+end
    if request.POST:
        dates = request.POST.get('dates', None)
        if dates:
            start, end = dates.split(' - ')
    summary_list  = UserEvents.objects.filter(date_id__range=(start, end),event__name='View Product')
    total = summary_list.aggregate(Sum('amount'))
    event_totals = summary_list.values('category__name').annotate(sum=Sum('amount'))
    stats_values = {}
    color_list = ['red','blue','orange']
    for each in event_totals:
        stats_values[each['category__name']] = [each['sum'],random.choice(color_list)]
    line_chart_data = []
    line_summary_list  = UserEvents.objects.filter(date_id__range=(start, end), event__name='View Product')
    line_summary_total = line_summary_list.values('date_id').annotate(sum=Sum('amount'))
    sales_line_data = []
    for each in line_summary_total:
        sales_line_data.append({"x":each['date_id'].strftime('%Y-%m-%d'),"y": int(each['sum'])})

    event_totals = summary_list.values('region__name').annotate(sum=Sum('amount'))
    pie_data = []
    for each in event_totals:
        pie_data.append({"key":str(each['region__name']),"count" : int(each['sum'])})

    loc_totals = summary_list.values('city__name').annotate(sum=Sum('amount'))
    loc_bar_data = []
    for each in loc_totals:
        loc_bar_data.append({"key":str(each['city__name']),"count" : int(each['sum'])})

    product_totals = summary_list.values('product__name').annotate(sum=Sum('amount'))
    product_bar_data = []
    for each in product_totals:
        product_bar_data.append({"key":str(each['product__name']),"count" : int(each['sum'])})


    vendor_totals = summary_list.values('vendor__name').annotate(sum=Sum('amount'))
    vendor_pie_data = []
    for each in vendor_totals:
        vendor_pie_data.append({"key":str(each['vendor__name']),"count" : int(each['sum'])})

    platform_totals = summary_list.values('platform__name').annotate(sum=Sum('amount'))
    platform_pie_data = []
    for each in platform_totals:
        platform_pie_data.append({"key":str(each['platform__name']),"count" : int(each['sum'])})

    browser_totals = summary_list.values('browser__name').annotate(sum=Sum('amount'))
    browser_pie_data = []
    for each in browser_totals:
        browser_pie_data.append({"key":str(each['browser__name']),"count" : int(each['sum'])})


    variables = {
    'total' : total['amount__sum'],
    'dates':dates,
    'start':start,
    'end':end,
    'stats_values' : stats_values,
    'sales_line_data' : sales_line_data,
    'pie_data' : pie_data,
    'loc_bar_data' : {"values" : loc_bar_data[:10],"names":['count']},
    'product_bar_data' : {"values" : product_bar_data[:10],"names":['count']},
    'vendor_pie_data' : vendor_pie_data,
    'platform_pie_data' : platform_pie_data,
    'browser_pie_data' : browser_pie_data

    }
    return render_to_response(template_name,  RequestContext(request,variables))