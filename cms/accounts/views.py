from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate

def check_mobile_number(mobile_number):
	flag = False
	try:
		user_obj = User.objects.get(mobile_number=mobile_number)
		if user_obj:
			flag = True
		else:
			flag = False
	except User.DoesNotExist as e:
		pass
	return flag
def check_membership_id(membership_id):
	flag = False
	try:
		user_obj = User.objects.filter(membership_id=membership_id)
		if user_obj:
			flag = True
		else:
			flag = False
	except User.DoesNotExist as e:
		pass
	return flag

def validate_login(**kwargs):
	user_obj = None
	try:
		user_obj = User.objects.get(username=kwargs['username'])
		if user_obj:
			if user_obj.check_password(kwargs['password']):
				user_obj = user_obj
			else:
				user_obj = None
		else:
			user_obj = None
	except User.DoesNotExist as e:
		pass
	return user_obj

