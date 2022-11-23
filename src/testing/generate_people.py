import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testing.settings')

import django
django.setup()

import random
from users import models
from faker import Faker
import random

fakegen = Faker()

def create_people():
    for i in range(10):
        new_name = fakegen.name().split(' ')

        u = models.User.objects.get_or_create(name=new_name[0],
                                          second_name=new_name[1],
                                          email=new_name[0] + new_name[1] + '@' + fakegen.domain_name())

if __name__ == '__main__':
    create_people()
    print('People created!')

