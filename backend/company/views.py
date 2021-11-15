import datetime

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view
import json

from .models import Company, CompanyReview
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import CompanySerializer, CompanyReviewSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class CompanyList(APIView):

    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

class CompanyDetail(APIView):
    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

class ReviewList(APIView):
    def get(self, request, company_id, format=None):
        review = self.get_object(company_id)
        serializer = CompanyReviewSerializer(review)
        now = datetime.datetime.now()
        print(review.pub_date-now)
        return Response(serializer.data)

    def get_object(self, company_id):
        try:
            return CompanyReview.objects.get(company__id=company_id)
        except CompanyReview.DoesNotExist:
            raise Http404

@api_view(['POST'])
def add_review(request):
    cid = request.data.get('cid')
    company = Company.objects.get(pk=cid)
    uid = request.data.get('uid')
    user = User.objects.get(pk=uid)
    review_obj = CompanyReview.objects.get_or_create(company=company, reviewer=user)[0]
    review_obj.job_title = request.data.get('job')
    review_obj.review_title = request.data.get('title')
    review_obj.review_cont = request.data.get('content')
    review_obj.rating = request.data.get('rating')
    review_obj.iv_difficulty = request.data.get('difficulty')
    review_obj.save()
    return JsonResponse({'msg': 'Successful', 'code': '200'}, json_dumps_params={'ensure_ascii': False})

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Company.objects.filter(Q(name__icontains=query))
        serializer = CompanySerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})