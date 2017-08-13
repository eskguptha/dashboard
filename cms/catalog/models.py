from __future__ import unicode_literals

from django.db import models
from accounts.models import User

class Devices(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Platforms(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Browsers(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Regions(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Cities(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Regions)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Events(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Vendor(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category)
    vendor = models.ForeignKey(Vendor)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s'%self.name

class UserEvents(models.Model):
    date_id = models.DateField()
    device = models.ForeignKey(Devices)
    platform = models.ForeignKey(Platforms)
    browser = models.ForeignKey(Browsers)
    region = models.ForeignKey(Regions)
    city = models.ForeignKey(Cities)
    event = models.ForeignKey(Events)
    category = models.ForeignKey(Category)
    vendor = models.ForeignKey(Vendor)
    product = models.ForeignKey(Products)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)