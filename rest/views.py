from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from student.models import Student, TakeLectures
from lecture.models import Lecture, Room, Beacon
from attendance.models import attendance
from .serializer import UserLectureSerializer,MessageSerializer, AttendSerializer
from django.http import HttpResponse, Http404
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
import datetime, time
import json
from django.core.exceptions import ObjectDoesNotExist

# 현재 날짜에 따른 요일 값 얻기
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
today_num = datetime.datetime.today().weekday()
today = day_of_week[today_num]
# 현재 시간(hour) 값
current_time = time.strftime('%H:%M', time.localtime(time.time()))

class UserLectureData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # 로그인 중인 학생 얻기(username)
        username = request.user.get_username()

        # 금일 학생의 수강 과목
        student = Student.objects.get(username=username)
        today_student_lectures = student.take_lectures.filter(day_of_the_week=today)
        # 현재 시간에 따른 수강해야할 강의 목록
        a = today_student_lectures.filter(start_time__gte="14:00")
        
        def get_lecture(a):
            b = a.order_by('start_time')
            if len(b) != 1:
                return b[0],b[1]
            else:
                return b[0], None

        if a.exists():
            current_lecture, next_lecture = get_lecture(a)
        else:
            current_lecture, next_lecture = None, None
        # 학생이 현재 들어야 할 수업 얻기 없으면 None
        if current_lecture is not None:
            # 현재 수강해야하는 강의의 강의실
            room_code = current_lecture.room_code
            building = Room.objects.get(code=room_code).building
            number = Room.objects.get(code=room_code).number
            room_name = building + str(" ") + number
            # 강의실에 대응되는 Beacon 값
            beacon_major = room_code.beacon.major
            beacon_minor = room_code.beacon.minor

            # REST API를 통해 Android로 전달할 data
            data = {'username':username, 'lecture':current_lecture.name, 'lecture_code':current_lecture.code, 'room_code':room_code, 'room_name':room_name, 'beacon_major':beacon_major, 'beacon_minor':beacon_minor, 'start_time':current_lecture.start_time,'end_time':current_lecture.end_time}
            serializer_class = UserLectureSerializer(data)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            data = {'username':username, 'message': '현재 수강할 강의가 없습니다.'}
            serializer_class = MessageSerializer(data)
            return Response(serializer_class.data, status=status.HTTP_204_NO_CONTENT)
    
class AttendData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        username = request.user.get_username()
        attend = attendance.objects.filter(username=username)
        serializer_class = AttendSerializer(attend, many=True)
        return Response(serializer_class.data)
    
    def post(self, request):
        ymd = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        a = request.data['result']
        try:
            attend = attendance.objects.get(time=ymd)
            b = attend.result
            c = json.loads(a)
            query = b.update(c)
            d = json.dumps(b)
            e = {'username':attend.username, 'lecture':attend.lecture_id, 'result': d}
            hi = "hi"
            serializer = AttendSerializer(attend, data=e)
            # 직접 유효성 검사
            if serializer.is_valid():
                # 저장
                serializer.save()       
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except ObjectDoesNotExist:
            serializer = AttendSerializer(data=request.data)
            if serializer.is_valid():   # 직접 유효성 검사
                serializer.save()       # 저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
