from django.contrib.auth.models import User

from .models import Company, CompanyReview
from rest_framework import serializers


class CompanyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyReview
        fields = ('id',
                  'job_title',
                  'review_title',
                  'review_cont',
                  'format_time',
                  'rating',
                  'iv_difficulty',
                  'get_reviewer',
        )

class CompanySerializer(serializers.ModelSerializer):
    review = CompanyReviewSerializer(many=True)
    class Meta:
        model = Company
        fields = ('id',
                  'name',
                  'intro',
                  'link',
                  'get_avg',
                  'get_review_num',
                  'review'
        )