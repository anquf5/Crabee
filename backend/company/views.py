import datetime

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json


from .models import Company, CompanyReview
from django.contrib.auth.models import User
from rest_framework import viewsets, status, authentication
from rest_framework import permissions
from .serializers import CompanySerializer, CompanyReviewSerializer, CompanyListSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

class indexCompanyList(APIView):
    def get(self, request, format=None):
        companies = Company.objects.filter(on_index=1)
        if len(companies) > 6:
            companies = companies[:6]
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)


class CompanyList(APIView):
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

    # get other companies
    def post(self, request, format=None):
        cid = request.data.get('company_id')
        companies = Company.objects.exclude(pk=cid)
        serializer = CompanyListSerializer(companies, many=True)
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
        return Response(serializer.data)

    def get_object(self, company_id):
        try:
            return CompanyReview.objects.get(company__id=company_id)
        except CompanyReview.DoesNotExist:
            raise Http404

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def add_review(request):
    cid = request.data.get('cid')
    company = Company.objects.get(pk=cid)
    review_obj = CompanyReview.objects.get_or_create(company=company, reviewer=request.user)[0]

    review_obj.job_title = request.data.get('job')
    review_obj.review_title = request.data.get('title')
    review_obj.review_cont = request.data.get('content')
    review_obj.rate = request.data.get('rate')
    difficulty = request.data.get('difficulty')
    if difficulty == 'Easy':
        review_obj.iv_difficulty = 0
    elif difficulty == 'Medium':
        review_obj.iv_difficulty = 1
    elif difficulty == 'Difficulty':
        review_obj.iv_difficulty = 2
    review_obj.save()

    return JsonResponse({'msg': 1, 'code': 200})

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        companies = Company.objects.filter(Q(name__icontains=query))
        serializer = CompanyListSerializer(companies, many=True)
        print(serializer)
        return Response(serializer.data)
    else:
        return Response({"companies": []})