from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
import os

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, blank=True, null=True)
    mobile_number = models.CharField(max_length=10,unique=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return '%s'%self.username