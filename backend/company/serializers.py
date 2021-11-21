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
    # def get_avatar(self, reviewer):
    #     avatar_query_set = reviewer.
    #     # user_avatar = UserProfile.objects.filter(user=user_obj)
    #     # if(len(user_avatar)>0):
    #     #     avatar = UserProfile.objects.get(user=user_obj).avatar
    #     return {'user': {'username': user_obj.username}}
        # else: return {'user': {'username': user_obj.username}}

# class AuthorSerializer(serializers.ModelSerializer):
#     # 该字段信息通过下方的get_books方法获取数据
#     books = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#     # 方法名称必须与上面定义的序列化字段一致，格式为："get_自定义字段名"
#     def get_books(self, author_obj):
#         # 通过book模型中的author字段的related_name反查出作者对应的图书集合
#         book_query_set = author_obj.author_book.all()
#         # 遍历图书集合获取图书的名称和出版时间，并返回
#         return {'count': book_query_set.count(),
#                 "data": [{'name': book_obj.book_name, 'publish_time': book_obj.publish_time} for
#                          book_obj in book_query_set]}

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