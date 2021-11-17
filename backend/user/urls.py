from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'user'

# urlpatterns = [path('user/login/', views.User.login, name='login'),
#                path('user/logout', views.User.logout, name='logout'),
#                # path('user/signup', views.User.signup, name='signup')
#
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)