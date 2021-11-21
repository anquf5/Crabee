from django.contrib.auth.models import User
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'userprofile'

urlpatterns = [path('userprof/upload', views.UserProfile.as_view(), name='userAvatar'),

]

urlpatterns = format_suffix_patterns(urlpatterns)