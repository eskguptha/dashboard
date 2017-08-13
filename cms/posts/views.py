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
from .models import Posts, Category, Banners
from django.template.defaultfilters import removetags


# Create your views here.

def randon_string_generator(stype, size):
    if stype == 'char':
        chars = string.ascii_uppercase + string.ascii_lowercase + ','
    elif stype == 'string':
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + ','
    elif stype == 'number':
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def home(request, template_name="index.html"):
    
    variables = {
    "post_list" : Posts.objects.filter(is_active=True).order_by('-updated_at'),
    "category_list" : Category.objects.filter(is_active=True).order_by('sortid'),
    "banner_list" :  Banners.objects.all()

    }
    return render_to_response(template_name,  RequestContext(request,variables))

def post_list(request, cname=None, template_name="posts/post_list.html"):
    category_obj = None
    post_obj = None
    keyword = None
    post_list = []
    if "keyword" in request.GET:
        keyword = request.GET['keyword']
    if cname:
        try:
            category_obj = Category.objects.get(slug=cname , is_active=True)
        except Category.DoesNotExist as e:
            pass
    if category_obj:
        if keyword:
            post_list = Posts.objects.filter(category=category_obj, slug__contains=keyword, is_active=True).order_by('-updated_at')
        else:
            post_list = Posts.objects.filter(category=category_obj, is_active=True).order_by('-updated_at')
    else:
        if keyword:
            post_list = Posts.objects.filter(slug__contains=keyword, is_active=True).order_by('-updated_at')
        else:
            post_list = Posts.objects.filter(is_active=True).order_by('-updated_at')
    
    
    
    variables = {
    "post_list":post_list,
    "category_obj":category_obj,
    "category_list" : Category.objects.filter(is_active=True).order_by('sortid'),

    }
    return render_to_response(template_name,  RequestContext(request,variables))

def post_detail(request,cname=None, pname=None, template_name="posts/post_detail.html"):
    
    post_obj = None
    post_list = []
    try:
        post_obj = Posts.objects.get(is_active=True, slug=pname )
    except Posts.DoesNotExist as e:
        pass

    category_obj = None
    try:
        category_obj = Category.objects.get(slug=post_obj.category.slug , is_active=True)
    except Category.DoesNotExist as e:
        pass
    if category_obj:
        post_list = Posts.objects.filter(category=category_obj, is_active=True).order_by('-updated_at')[:20]
    
    variables = {
    "post_obj":post_obj,
    "category_list" : Category.objects.filter(is_active=True).order_by('sortid'),
    "post_list" : post_list

    }
    return render_to_response(template_name,  RequestContext(request,variables))


def search(request, template_name="posts/search.html"):
    keyword = None
    if "keyword" in request.GET:
        keyword = request.GET['keyword']
    if keyword:
        category_obj = None
        try:
            category_obj = Category.objects.filter(Q(is_active=True) & Q(Q(name__contains=keyword) | Q(slug__contains=keyword)))
        except Category.DoesNotExist as e:
            pass
        if category_obj:
            post_list = Posts.objects.filter( Q(is_active=True) & Q(Q(name__contains=keyword) |Q(slug__contains=keyword) | Q(description__contains=keyword) | Q(category__in=category_obj))).order_by('-updated_at')
        else:
            post_list = Posts.objects.filter( Q(is_active=True) & Q(Q(name__contains=keyword) |Q(slug__contains=keyword) | Q(description__contains=keyword) )).order_by('-updated_at')

    else:
        post_list = Posts.objects.filter(is_active=True).order_by('-updated_at'),
    
    variables = {
    "post_list":post_list,
    "keyword" : keyword,
    "category_list" : Category.objects.filter(is_active=True).order_by('sortid'),

    }
    return render_to_response(template_name,  RequestContext(request,variables))