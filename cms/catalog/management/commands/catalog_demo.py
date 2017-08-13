from django.core.management.base import BaseCommand, CommandError
from catalog.models import *
from accounts.models import *
import random
from django.db import IntegrityError
import string
from datetime import date, timedelta


def randon_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "string":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

class Command(BaseCommand):
    help = 'Demo Insert'

    def handle(self, *args, **options):
        device_list = ['Desktop', 'Mobile', 'Tablet']
        os_list = ['Windows','Mac','Andriod']
        browser_list = ['Firefox','Chrome','Opera','Safari','IE','UC Browser']
        loc_list = {
         "California"  :['Los Angeles', 'San Diego', 'San Jose', 'San Francisco','Fresno'],
         "New York" : ['Rochester','Yonkers','Syracuse','Buffalo'],
         "Texas" : ['Houston','San Antonio','Dallas','Austin','Fort Worth'],
         "Florida" : ['Miami','Tampa','Orlando','St. Petersburg','Hialeah'],
         "Virginia" : ['Richmond','Varginia Beach','Chesapeake','Richmond']
        }
        event_list = ['View Product', "Add to Cart", "Wishlist","Buy Product"]
        category_list = {
            "Mobiles" : ['Iphone','Nokia','Samsung','Motorola','LG','NEXUS','OnePlus'],
            "Electronics" : ['LG TV','Samsung TV','Air cooler','Sansui AC','Sony Brvia','LG Fridze'],
            "Footwear" :['Nike Shoes', 'Adidas shoes','Puma Shoes','Woodland'],
            "Means Wear" :['Jeans','Cotton Jeans','Formal Shirt','Cotton Shirt','Short','Trouser','Soxes','Kurta','Sherwany','Suit'],
            "Accessories" :['Mobile charger', 'Pen Drive', 'Pen','Cricket Ball', 'Foot ball','Basket Ball'],
        }

        vendor_list = ["Vendor %s"%i for i in range(5)]
        for item in device_list:
            try:
                Devices.objects.create(name=item)
            except IntegrityError as error:
                print error

        for item in os_list:
            try:
                Platforms.objects.create(name=item)
            except IntegrityError as error:
                print error

        for item in browser_list:
            try:
                Browsers.objects.create(name=item)
            except IntegrityError as error:
                print error

        for reg, city_list in loc_list.items():
            try:
                reg_obj  = Regions.objects.create(name=reg)
                try:
                    for city in city_list:
                        Cities.objects.create(name=city, region=reg_obj)
                except IntegrityError as error:
                    print error
            except IntegrityError as error:
                print error

        for item in event_list:
            try:
                Events.objects.create(name=item)
            except IntegrityError as error:
                print error

        for item in vendor_list:
            try:
                Vendor.objects.create(name=item)
            except IntegrityError as error:
                print error

        for cat, cat_list in category_list.items():
            try:
                cat_obj = Category.objects.create(name=cat)
                try:
                    for p in cat_list:
                        Products.objects.create(name=p, category=cat_obj, price=random.randint(10,50),vendor=random.choice(Vendor.objects.all()))
                except IntegrityError as error:
                    print error
            except IntegrityError as error:
                print error
        for i in range(100):
            try:
                user_obj =  User.objects.create(
                    username = randon_string_generator(random.randint(3,10), 'string'),
                    first_name = randon_string_generator(random.randint(1,5), 'string'),
                    last_name = randon_string_generator(random.randint(1,3), 'string'),
                    mobile_number = randon_string_generator(10, 'number')
                    )
            except IntegrityError as error:
                print error

        start_date = date(2017, 8,1)
        end_date = date(2017, 8, 8)
        delta = end_date - start_date
        date_list = []
        for i in range(delta.days + 1):
            date_list.append(start_date + timedelta(days=i))

        user_list = User.objects.all()
        city_list =  Cities.objects.all()
        product_list = Products.objects.all()
        for each_date in date_list:
            for i in range(1, 5):
                user_obj = random.choice(user_list)
                city_obj = random.choice(city_list)
                product_obj = random.choice(product_list)
                UserEvents.objects.create(
                    device=random.choice(Devices.objects.all()),
                    browser=random.choice(Browsers.objects.all()),
                    platform=random.choice(Platforms.objects.all()),
                    city=city_obj,
                    region= city_obj.region,
                    product=product_obj,
                    category=product_obj.category,
                    amount=product_obj.price,
                    vendor=product_obj.vendor,
                    event=random.choice(Events.objects.all()),
                    date_id=each_date,
                    user=user_obj
                    )






