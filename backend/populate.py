import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crabee_project.settings')
import time
import django
django.setup()
from django.conf import settings
from django.core.files.images import ImageFile
from company.models import *

companies = [{'name': 'Amazon',
              'intro': 'a company',
              'link': 'https://www.amazon.jobs/',
              'logo': 'companyLogo/Amazon.jpg',
              'on_index': True},
             {'name': 'Google',
              'intro': 'b company',
              'link': 'https://careers.google.com/',
              'logo': 'companyLogo/Google.jpg',
              'on_index': True},
             {'name': 'LinkedIn',
              'intro': 'c company',
              'link':'https://www.linkedin.com/feed/',
              'logo': 'companyLogo/LinkedIn.jpg',
              'on_index': True},
            {'name': 'CVS Health',
              'intro': 'd company',
              'link':'https://jobs.cvshealth.com/',
              'logo': 'companyLogo/CVS_Health.jpg',
              'on_index': True},
            {'name': 'Walmart',
              'intro': 'e company',
              'link':'https://careers.walmart.com/',
              'logo': 'companyLogo/Walmart.jpg',
              'on_index': True},
            {'name': 'Apple',
              'intro': 'e company',
              'link':'https://www.apple.com/careers/',
              'logo': 'companyLogo/Apple.jpg',
              'on_index': True},
            {'name': 'Microsoft',
              'intro': 'f company',
              'link':'https://news.microsoft.com/',
              'logo': 'companyLogo/Microsoft.jpg',
              'on_index': False},
            {'name': 'Tesla',
              'intro': 'g company',
              'link':'https://www.tesla.com/careers',
              'logo': 'companyLogo/Tesla.jpg',
              'on_index': False},
            {'name': 'Meta',
              'intro': 'h company',
              'link':'https://www.facebookcareers.com/',
              'logo': 'companyLogo/Meta.jpg',
              'on_index': False},
            {'name': 'NVIDIA',
              'intro': 'i company',
              'link':'https://www.nvidia.com/',
              'logo': 'companyLogo/NVIDIA.jpg',
              'on_index': False},
            {'name': 'NVIDIA',
              'intro': 'i company',
              'link':'https://www.nvidia.com/',
              'logo': 'companyLogo/NVIDIA.jpg',
              'on_index': False},
            {'name': 'TSMC',
              'intro': 'j company',
              'link':'https://www.tsmc.com/static/english/careers/index.htm',
              'logo': 'companyLogo/tsmc.jpg',
              'on_index': False},
            {'name': 'Tencent',
              'intro': 'k company',
              'link':'https://www.tencent.com/',
              'logo': 'companyLogo/Tencent.jpg',
              'on_index': False},
            {'name': 'J.P.Morgan',
              'intro': 'l company',
              'link':'https://www.jpmorgan.com/global',
              'logo': 'companyLogo/jpmorgan.jpg',
              'on_index': False},
            {'name': 'VISA',
              'intro': 'm company',
              'link':'https://usa.visa.com/careers.html',
              'logo': 'companyLogo/visa.jpg',
              'on_index': False},
            {'name': 'The Home Depot',
              'intro': 'n company',
              'link':'https://careers.homedepot.com/',
              'logo': 'companyLogo/The Home Depot.jpg',
              'on_index': False},
            {'name': 'Johnson & Johnson',
              'intro': 'o company',
              'link':'https://www.careers.jnj.com/',
              'logo': 'companyLogo/Johnson & Johnson.jpg',
              'on_index': False},
            {'name': 'Samsung Electronics',
              'intro': 'p company',
              'link':'https://www.samsung.com/',
              'logo': 'companyLogo/Samsung Electronics.jpg',
              'on_index': False},
            {'name': 'LVMH',
              'intro': 'q company',
              'link':'https://www.lvmh.com/',
              'logo': 'companyLogo/LVMH.jpg',
              'on_index': False},
            {'name': 'Bank of America',
              'intro': 'r company',
              'link':'https://www.bankofamerica.com/',
              'logo': 'companyLogo/Bank of America.jpg',
              'on_index': False},
            {'name': 'Alibaba Group',
              'intro': 's company',
              'link':'https://www.alibabagroup.com/',
              'logo': 'companyLogo/Alibaba Group.jpg',
              'on_index': False},
            {'name': 'Nestlé',
              'intro': 't company',
              'link':'https://www.nestle.com/',
              'logo': 'companyLogo/Nestlé.jpg',
              'on_index': False},
             ]
users = [
    {'username': 'diablo', 'password': 'test123', 'email': 'diablo@test.com', 'image': 'avatar/diablo.png'},
    {'username': 'Augenstern', 'password': 'test123', 'email': 'Augenstern@test.com',
     'image': 'avatar/augenstern.jpg'},
    {'username': 'yuuki', 'password': 'test123', 'email': 'yuuki@test.com', 'image': 'avatar/yuuki.jpg'},
    {'username': 'flechazo', 'password': 'test123', 'email': 'flechazo@test.com', 'image': 'avatar/flechazo.jpg'},
    {'username': 'espoir', 'password': 'test123', 'email': 'espoir@test.com', 'image': 'avatar/espoir.jpg'},
]

reviews = [
    {'company_id': 1,'job_title': "Java Developer",'review_title': "Lots to learn",
     'review_cont': "Amazon is a great company to learn, where management are open to discussions at any time and a healthy work/life balance. The share the company includes in the compensation make the employee willing to stay longer.",
     'rate': 4,'iv_difficulty': 1,'reviewer_id': 1,
     },
    {'company_id': 1,'job_title': "Python Developer",'review_title': "Productive",
     'review_cont': "Amazon is a fun place to work, with good training that allows you to do your job efficiently and safely. The supervisors are helpful and try and sort out any problems you may have to the best of their pay grade. Working at amazon you get to learn a lot of new skills about logistics and warehousing. If you want to progress you can by demonstrating a good work ethic and learning capabilities",
     'rate': 5,'iv_difficulty': 2,'reviewer_id': 2,
     },
    {'company_id': 1,'job_title': "Python Developer",'review_title': "Hard work",
     'review_cont': "Been here a few weeks now. Make no mistake about the job. It's continuous work for 10hrs, repetitive and you're on your feet all day. Management seem ok and very helpful with any enquiries you may have. All in all it seems a good place to work. I've no complaints as such.",
     'rate': 4,'iv_difficulty': 2,'reviewer_id': 4,
     },
    {'company_id': 1,'job_title': "Python Developer",'review_title': "Neither bad nor good",
     'review_cont': "Amazon pays very good money especially if there’s overtime. I am impressed with how the warehouse works. It’s all worked out to the smallest detail and little room for things to go wrong. Simple job. Many different positions available. I just wish that I could stay longer but apparently they rarely extend contracts and very rarely offer permanent positions.",
     'rate': 5,'iv_difficulty': 2,'reviewer_id': 3,
     },
]

def populate():
    for company in companies:
        add_company(company['name'], company['intro'], company['link'], company['logo'], company['on_index'])
    for user in users:
        image = None
        if 'image' in user.keys():
            image = user['image']

        user = add_user(user['username'], user['password'], user['email'], image)

    for review in reviews:
         add_review(review['company_id'], review['job_title'], review['review_title'], review['review_cont'], review['rate'], review['iv_difficulty'], review['reviewer_id'])

def add_company(name, intro, link, logo, on_index):
    p = Company.objects.get_or_create(name=name, intro=intro, link=link, img=logo, on_index= on_index)[0]
    p.save()
    print(f'- Populate: company {p} added')
    return p

def add_user(username, password, email, image=None):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.set_password(password)
    user.save()
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    userprofile.has_confirmed = True
    if image:
        userprofile.image = os.path.join(image)
        # print(f'- add image {image}')

    userprofile.save()
    return user

def add_review(cid,job_title,review_title,review_cont,rate, iv_difficulty, reviewer_id):
    review = CompanyReview.objects.get_or_create(company_id=cid, job_title = job_title, reviewer_id=reviewer_id, review_title=review_title, review_cont=review_cont, rate=rate, iv_difficulty=iv_difficulty)[0]
    return review.save()


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
