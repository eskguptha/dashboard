from django.db import models
from accounts.models import User


class Banners(models.Model):
    name = models.CharField(max_length=30, unique=True)
    sortid = models.IntegerField(default=1)
    image = models.ImageField(upload_to='banners')
    url = models.TextField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Banners"

    def __str__(self):
        return '%s'%self.name

class FlashNews(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=50, blank=True)
    sortid = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "FlashNews"

    def __str__(self):
        return '%s'%self.name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=50, blank=True)
    sortid = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = self.name.strip().replace(' ','-').lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return '%s'%self.name



class Posts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=125, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        self.slug = self.name.strip().replace(' ','-').lower()
        super(Posts, self).save(*args, **kwargs)

    def __str__(self):
        return '%s'%self.name


class Ratings(models.Model):
    rating = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)
    post = models.ForeignKey(Posts)
    comments = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Ratings"

    def __str__(self):
        return '%s'%self.rating