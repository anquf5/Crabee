import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Avg
from django.template.defaultfilters import slugify

from userprofile.models import UserProfile

TITLE_MAX_LENGTH = 128
CONTENT_MAX_LENGTH = 1000
class Company(models.Model):
    name = models.CharField(max_length=32)
    intro = models.CharField(max_length=1000)
    link = models.URLField(blank=True)
    img =models.ImageField(upload_to='companyLogo/', blank=True, null=True)

    class Meta:
        ordering = ('id',)

    def get_avg(self):
        avg = CompanyReview.objects.filter(company=self).aggregate(Avg('rate'))['rate__avg']
        return int(avg) if avg else 0

    def get_review_num(self):
        num = CompanyReview.objects.filter(company=self).count()
        return num

    def get_absolute_url(self):
        return f'/company/{self.id}/'


    def get_image(self):
        if self.img:
            return 'http://127.0.0.1:8000' + self.img.url
        else: return ''

    def __str__(self):
        return self.name

class CompanyReview(models.Model):
    JOBTITLE_MAX_LENGTH = 32
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="review")
    job_title = models.CharField(max_length=JOBTITLE_MAX_LENGTH)
    review_title = models.CharField(max_length=TITLE_MAX_LENGTH)
    review_cont = models.CharField(max_length=CONTENT_MAX_LENGTH) # review content
    pub_time = models.DateTimeField(auto_now=True) # publish date
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    iv_difficulty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], default=0) # interview difficulty
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")

    class Meta:
        ordering = ('-pub_time',)

    def get_reviewer(self):
        u = self.reviewer.username
        return u

    def get_user_avatar(self):
        u = UserProfile.objects.filter(user = self.reviewer).all()
        if u.exists():
            return u[0].__str__()
        else:
            return ''

    def get_pubtime(self):
        t = self.pub_time.strftime("%Y-%m-%d %H:%M")
        return t

    def __str__(self):
        return self.review_title