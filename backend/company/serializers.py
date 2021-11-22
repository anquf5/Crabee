from django.contrib.auth.models import User

from userprofile.models import UserProfile
from .models import Company, CompanyReview
from rest_framework import serializers

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id',
                  'name',
                  'get_image',
                  'get_absolute_url',
                  'get_review_num',
                  'get_avg'
                  )


class CompanyReviewSerializer(serializers.ModelSerializer):
    # avatar = serializers.SerializerMethodField()
    class Meta:
        model = CompanyReview
        fields = ('id',
                  'job_title',
                  'review_title',
                  'review_cont',
                  'get_pubtime',
                  'rate',
                  'iv_difficulty',
                  'get_reviewer',
                  'get_user_avatar',
        )

class CompanySerializer(serializers.ModelSerializer):
    review = CompanyReviewSerializer(many=True)
    class Meta:
        model = Company
        fields = ('id',
                  'name',
                  'intro',
                  'link',
                  'get_image',
                  'get_avg',
                  'get_review_num',
                  'review',
        )