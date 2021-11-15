from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Avg
from django.template.defaultfilters import slugify

TITLE_MAX_LENGTH = 128
CONTENT_MAX_LENGTH = 1000
class Company(models.Model):
    name = models.CharField(max_length=32)
    intro = models.CharField(max_length=256)
    link = models.URLField(blank=True)
    # img = models.ImageField(upload_to='company_logos', blank=True, null=True)

    class Meta:
        ordering = ('id',)

    def get_avg(self):
        avg = CompanyReview.objects.filter(company=self).aggregate(Avg('rating'))['rating__avg']
        return int(avg) if avg else 0

    def get_review_num(self):
        num = CompanyReview.objects.filter(company=self).count()
        return num
    # def get_image(self):
    #     if self.img:
    #         return 'http://127.0.0.1:8000' + self.img.url

    # def get_difficulty(self):
    #     dif = CompanyReview.objects.filter(company=self).aggregate(Avg('iv_difficulty'))['difficulty__avg']
    #     return int(dif) if dif else 0

    def __str__(self):
        return self.name

class CompanyReview(models.Model):
    JOBTITLE_MAX_LENGTH = 32
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="review")
    job_title = models.CharField(max_length=JOBTITLE_MAX_LENGTH)
    review_title = models.CharField(max_length=TITLE_MAX_LENGTH)
    review_cont = models.CharField(max_length=CONTENT_MAX_LENGTH) # review content
    pub_date = models.DateTimeField(auto_now=True) # publish date
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    iv_difficulty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], default=0) # interview difficulty
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_date',)

    def get_reviewer(self):
        un = User.objects.get(pk=self.reviewer_id).username
        return un

    def __str__(self):
        return self.review_title