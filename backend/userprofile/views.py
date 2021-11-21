from django.shortcuts import render

# Create your views here.
import datetime

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json


from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework import viewsets, status, authentication
from rest_framework import permissions
from .serializers import UserProfileSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

@authentication_classes([authentication.TokenAuthentication])
class UserProfile(APIView):
    def get(self, request, format=None):
        try:
            userprof = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(userprof)
            return Response(serializer.data)
        except:
            return Response({'get_image': False})
