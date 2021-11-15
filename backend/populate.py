import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crabee_project.settings')
import time
import django
django.setup()
from django.conf import settings
from django.core.files.images import ImageFile
from company.models import *

companies = [{'name': 'Google', 'intro': 'a company', 'link': 'www.google.com'},
             {'name': 'Amazon', 'intro': 'b company', 'link': 'www.amazon.com'}
             ]

users = [{'username': 'diablo', 'password': 'test123', 'email': 'diablo@test.com'},
        {'username': 'Augenstern', 'password': 'test123', 'email': 'Augenstern@test.com'},
        {'username': 'yuuki', 'password': 'test123', 'email': 'yuuki@test.com'},
        {'username': 'flechazo', 'password': 'test123', 'email': 'flechazo@test.com'},
        {'username': 'espoir', 'password': 'test123', 'email': 'espoir@test.com'},
]

def populate():
    for company in companies:
        add_company(company['name'], company['intro'], company['link'])
    for user in users:
        add_user(user['username'], user['password'], user['email'])




def add_company(name, intro, link):
    p = Company.objects.get_or_create(name=name, intro=intro, link=link)[0]
    p.save()
    print(f'- Populate: company {p} added')
    return p

def add_user(username, password, email):
    p = User.objects.get_or_create(username=username, password=password, email=email)[0]
    p.save()
    print(f'- Populate: company {p} added')
    return p


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
