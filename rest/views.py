from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from student.models import enroll
from lecture.models import Lecture, Room, Beacon
from .serializer import UserSerializer
from django.http import HttpResponse, Http404
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
import datetime
import json

class UserList(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # 현재 날짜에 따른 요일 값 얻기
        day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        today_num = datetime.datetime.today().weekday()
        today = day_of_week[today_num]
        # 현재 시간(hour) 값
        current_time = datetime.datetime.now().hour
        # 로그인 중인 학생 얻기(username)
        username = request.user.get_username()

        # 얻은 학생의 수강하는 과목 얻기
        user_enroll = enroll.objects.get(user__username=username)
        
        # 현재 시작할 강의 찾기 ex) 현재 시간 08:00 현재 요일 : 월요일
        # 월요일 오전에 시작하는 강의 찾기
        def get_lecture_by_today_current_time(Lecture):
            if current_time <= 12:
                # 그 날 오전 강의 return
                return Lecture.objects.filter(day_of_the_week=today).filter(start_time="09:00")
            else:
                # 그 날 오후 강의 return
                return Lecture.objects.filter(day_of_the_week=today).filter(start_time="14:00")
        # 그 날의 오전 강의        
        day_lecture = get_lecture_by_today_current_time(Lecture)
        # 
        def get_now_lecture(user_enroll,day_lecture):
            for l in user_enroll.lecture_list.all():
                for ll in day_lecture.all():
                    if str(ll) == str(l):
                        return l
                    else:
                        continue
        now_lecture = get_now_lecture(user_enroll,day_lecture)
        # 강의실로 접근
        now_room = now_lecture.room_code
        # Beacon 값
        now_room_beacon_major = now_lecture.room_code.beacon.beacon_major
        now_room_beacon_minor = now_lecture.room_code.beacon.beacon_minor
        user_data = {'username':username,'now_lecture':now_lecture.name,'now_room':now_room.room_code,'now_room_beacon_major':now_room_beacon_major,'now_room_beacon_minor':now_room_beacon_minor}
        serializer_class = UserSerializer(user_data)
        return Response(serializer_class.data)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
