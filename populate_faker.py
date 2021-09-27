


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from faker import Faker
import random
fake = Faker()

topic = ['Search', 'Social', 'Marketplace', 'News', 'Games']
from AppTwo.models import AccessRecord, Topic, Webpage

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t


def populate(N):
    for entry in range(N):
        top = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)


if __name__ == '__main__':
    print('d')
    populate(20)
    print('populating complete')
