import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from first_app.models import AcessRecord,Topic,WebPage
from faker import Faker
import random

fakegen=Faker()
topics=['Health','Sports','Education','News','Politics','Marketplace','Social']

def add_topic():
    t=Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for i in range(n):
        fake_name=fakegen.company()
        fake_url=fakegen.url()
        fake_date=fakegen.date()

        top=add_topic()

        webpg=WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acessrcd=AcessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print('populating script')
    populate(5)
    print('population complete')
