from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from student.models import enroll
from lecture.models import Lecture, Room, Beacon
from .serializer import UserLectureSerializer,UserListSerializer,hi
from django.http import HttpResponse, Http404
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
import datetime
import json

class UserLectureData(APIView):
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
        # 학생이 그 날 듣는 수업 얻기 없으면 None
        def get_now_lecture(user_enroll,day_lecture):
            for l in user_enroll.lecture_list.all():
                for ll in day_lecture.all():
                    if str(ll) == str(l):
                        return l
                    else:
                        continue
        
        now_lecture = get_now_lecture(user_enroll,day_lecture)

        if now_lecture is not None:
            # 강의실로 접근
            now_room = now_lecture.room_code
            # Beacon 값
            now_room_beacon_major = now_lecture.room_code.beacon.beacon_major
            now_room_beacon_minor = now_lecture.room_code.beacon.beacon_minor
            user_data = {'username':username,'now_lecture':now_lecture.name,'now_lecture_code':now_lecture.lecture_code,'now_room':now_room.room_code,'now_room_beacon_major':now_room_beacon_major,'now_room_beacon_minor':now_room_beacon_minor,'start_time':now_lecture.start_time,'end_time':now_lecture.end_time}
            serializer_class = UserLectureSerializer(user_data)
            return Response(serializer_class.data)
        else:
            user_data = {'username':username,'now_lecture':None,'now_room':None,'now_room_beacon_major':None,'now_room_beacon_minor':None}
            serializer_class = UserLectureSerializer(user_data)
            return Response(serializer_class.data)

# 해당 강의에 대한 학생 리스트와 사진 반환?
class UserList(APIView):
    def get(self, request):
        # 현재 날짜에 따른 요일 값 얻기
        day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        today_num = datetime.datetime.today().weekday()
        today = day_of_week[today_num]
        # 현재 시간(hour) 값
        current_time = datetime.datetime.now().hour
        def get_lecture_by_today_current_time(Lecture):
            if current_time <= 12:
                # 그 날 오전 강의 return
                return Lecture.objects.filter(day_of_the_week=today).filter(start_time="09:00")
            else:
                # 그 날 오후 강의 return
                return Lecture.objects.filter(day_of_the_week=today).filter(start_time="14:00")
        # 그 날의 오전 강의        
        day_lecture = get_lecture_by_today_current_time(Lecture)
        a = day_lecture.get(room_code="R002")
        aid = a.id
        enrollqueryset = enroll.objects.filter(lecture_list__id=aid)
        
        # serializer_class = hi(enrollqueryset, many=True)
        # return Response(serializer_class.data)
        uudata = []
        for z in enrollqueryset:
            udata = {'username':z.user.username,'userface':z.user.student.photo}
            # uudata.append(list(udata.items()))
            # for key, value in udata.items():
            #     uudata.append((key,value))

        serializer_class = UserListSerializer(udata)
        return Response(serializer_class.data)
        # serializer_class = UserListSerializer(dict(uudata), many=True)
        # return Response(serializer_class.data)




class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
