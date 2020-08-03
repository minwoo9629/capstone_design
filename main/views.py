from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User, Group
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import UserSerializer
from django.http import HttpResponse, JsonResponse
#-------------------------------------------------

import datetime
# from student.models import enroll
from lecture.models import Lecture, Room, Beacon
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from attendance.models import attendance

# Create your views here.
def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.groups.filter(name = 'student').exists():
                return redirect('student')
            elif user.groups.filter(name = 'professor').exists():
                return redirect('prof')    
            else:
                return redirect('manager')
            # 로그인 성공한 경우
        else:
            return render(request, 'main.html', {'error':'username or password is incorrect.'})
            # 로그인에 실패했을 경우 ERROR Message
    else:
        return render(request, 'main.html')
        # GET 요청인 경우 로그인 화면
    return render(request,'main.html')
