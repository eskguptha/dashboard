from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.sites.models import Site
import random

from django.db import transaction, IntegrityError
from posts.models import *
from posts.views import *
from accounts.models import *
from django.contrib.auth.models import Group
from django.conf import settings

class Command(BaseCommand):
    help = 'Insert test data'

    def handle(self, *args, **options):
        site_obj = Site.objects.get(id=2)
        site_obj.name = "CMS"
        site_obj.domain = "http://127.0.0.1:8000"
        site_obj.save()
        
        # category
        categories = ['News','Entertainment','Education','Healthcare','Sports']
        sort_id = 1
        for each in categories:
            try:
                cat_obj = Category()
                cat_obj.name = each
                cat_obj.sortid = sort_id
                sort_id = sort_id+1
                cat_obj.description =  ', '.join(randon_string_generator('char', 500).split(','))
                cat_obj.save()
            except (IntegrityError) as e:
                pass
        categories_list = Category.objects.all()

        # Posts
        for i in range(1,100):
            try:
                post_obj = Posts()
                paragraph = ' '.join(randon_string_generator('char', 30).split(','))
                x = random.randint(1,5)
                p = [paragraph[i: i + x] for i in range(0, len(paragraph), x)]
                post_obj.name = ' '.join(p)
                paragraph = ' '.join(randon_string_generator('char', 2000).split(','))
                x = random.randint(3,7)
                p = [paragraph[i: i + x] for i in range(0, len(paragraph), x)]
                post_obj.description = ' '.join(p)
                post_obj.category = random.choice(categories_list)
                post_obj.save()
            except (IntegrityError) as e:
                pass

        post_list = Posts.objects.all()
        
        # Ratings
        for i in range(1,100):
            try:
                rating_obj = Ratings()
                rating_obj.name = ' '.join(randon_string_generator('char', 10).split(','))
                paragraph = ' '.join(randon_string_generator('char', 500).split(','))
                x = 5
                p = [paragraph[i: i + x] for i in range(0, len(paragraph), x)]
                rating_obj.comments = ' '.join(p)
                rating_obj.rating = random.randint(1,5)
                rating_obj.post = random.choice(post_list)
                rating_obj.save()
            except (IntegrityError) as e:
                pass

        # # Flashnews
        # for i in range(1,10):
        #     try:
        #         flash_obj = FlashNews()
        #         flash_obj.name = ' '.join(randon_string_generator('char', 10).split(','))
        #         flash_obj.description = ', '.join(randon_string_generator('char', 300).split(','))
        #         flash_obj.sortid = random.randint(1,5)
        #         flash_obj.save()
        #     except (IntegrityError) as e:
        #         pass
