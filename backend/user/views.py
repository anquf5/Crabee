import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class User(APIView):
    def get_status(request):
        if request.user.is_authenticated:
            return JsonResponse({
                "status": 0,
                "username": str(request.user),
                "email": str(request.user.email),
            })
        else:
            return JsonResponse({
                "status": 1
            })

    @api_view(['POST'])
    def login(request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is not None and password is not None:
            is_login = authenticate(request, username=username, password=password)

            if is_login:
                login(request,is_login)
                # session = is_login.objects.get('session')
                return JsonResponse({'username': username, 'act': 'Log in', 'msg': 1})
            else:
                return JsonResponse({'username': username, 'act': 'Log in', 'msg': 0})
        else:
            return JsonResponse({'username': username, 'act': 'Log in', 'msg': -1})

    def logout(request):
        logout(request)
        return JsonResponse({'act': 'Log out', 'msg': 1})

    # @api_view(['POST'])
    # def signup(request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     email = request.data.get('email')
    #     if username is not None and password is not None and email is not None:
    #         try:
    #             user = User.objects.get()
