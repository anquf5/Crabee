
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'company'

urlpatterns = [path('company/', views.CompanyList.as_view(), name='company_list'),
               path('index_company/', views.indexCompanyList.as_view(), name='index_company'),
               path('company/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
               # path('company_review/<int:company_id>/', views.ReviewList.as_view(), name='company_review'),
               path('company_review/add/', views.add_review, name='add_review'),
               path('company/search/', views.search, name='search_company')
]

urlpatterns = format_suffix_patterns(urlpatterns)