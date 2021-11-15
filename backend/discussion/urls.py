from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'discussion'

urlpatterns = [path('topic/', views.TopicList.as_view(), name='topic'),
               path('topic/add/', views.add_topic, name="add_topic"),
               path('topic/<int:pk>/', views.TopicDetail.as_view(), name='topic_detail'),
               path('topic/reply/', views.add_reply, name="add_reply")
]