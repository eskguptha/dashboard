# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('sortid', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to=b'banners')),
                ('url', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('slug', models.CharField(max_length=50, blank=True)),
                ('sortid', models.IntegerField(default=1)),
                ('description', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='FlashNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('slug', models.CharField(max_length=50, blank=True)),
                ('sortid', models.IntegerField(default=1)),
                ('description', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'FlashNews',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('slug', models.CharField(max_length=125, blank=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'posts', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='posts.Category')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('name', models.CharField(unique=True, max_length=100)),
                ('comments', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='posts.Posts')),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
