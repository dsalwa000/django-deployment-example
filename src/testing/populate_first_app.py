import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testing.settings')

import django
django.setup()

import random
from first.models import *
from faker import Faker

fakegen = Faker()
topics = ['Secarch', 'Social', 'Martketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)

        acc_rec = Access.objects.get_or_create(name='new', second='second')[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('Populating complete')
