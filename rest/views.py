from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from student.models import Student, TakeLectures
from lecture.models import Lecture, Room, Beacon
from attendance.models import attendance, facial_attendance, userlog
from .serializer import MessageSerializer, AttendSerializer, LectureSerializer, Facial_AttendSerializer, FinalResultSerializer, LogSerializer
from django.http import HttpResponse, Http404
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
import datetime, time, json
from django.core.exceptions import ObjectDoesNotExist

def final_result_function(lecture_id, username,ymd):
    attend = attendance.objects.filter(time=ymd).filter(lecture_id=lecture_id).get(username=username)
    facial_attend = facial_attendance.objects.filter(time=ymd).filter(lecture_id=lecture_id).get(username=username)
    
    attend_list = []
    facial_attend_list = []
    final_result_list = []

    dict_attend = {}
    dict_facial_attend = {}
    dict_attend = json.loads(attend.result)
    dict_facial_attend = json.loads(facial_attend.result)
    
    for key in dict_attend.keys():
        attend_list.append(dict_attend[key])

    for key in dict_facial_attend.keys():
        facial_attend_list.append(dict_facial_attend[key])

    for i,j in zip(attend_list,facial_attend_list):
        if i == j:
            final_result_list.append(i)
        else:
            final_result_list.append("ABSENT")

    if len(list(set(final_result_list))) == 2:
        attend.final_result = "지각"
    
    else:
        if list(set(final_result_list))[0] == "ATTEND":
            attend.final_result = "출석"
        else:
            attend.final_result = "결석"
    attend.save()

# 현재 날짜에 따른 요일 값 얻기
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
today_num = datetime.datetime.today().weekday()
today = day_of_week[today_num]
# 현재 시간(hour) 값
current_time = time.strftime('%H:%M', time.localtime(time.time()))

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'uuid' : user.student.college.uuid,
        })
        


class UserLectureData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # 로그인 중인 학생 얻기(username)
        username = request.user.get_username()

        # 금일 학생의 수강 과목
        student = Student.objects.get(username=username)
        lecture_list = student.take_lectures.filter(day_of_the_week=today)
        # 현재 시간에 따른 수강해야할 강의 목록
        # lecture_list = today_student_lectures.filter(end_time__gte="14:00")
        
        def get_lecture(lecture_list):
            sequence = []
            lecture_id = []
            order_lecture_list = lecture_list.order_by('start_time')
            for num in range(len(order_lecture_list)):
                sequence.append(num+1)

            for lecture in order_lecture_list:
                lecture_id.append(lecture.id)
            
            lecture_data = dict(zip(sequence,lecture_id))
            return lecture_data

        if lecture_list is not None:
            lecture_data = get_lecture(lecture_list)
            return Response(lecture_data, status=status.HTTP_200_OK)
        else:
            data = {'message': '현재 수강할 강의가 없습니다.'}
            serializer_class = MessageSerializer(data)
            return Response(serializer_class.data, status=status.HTTP_204_NO_CONTENT) 
            

class LectureData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        username = request.user.get_username()
        lecture_id = request.data['lecture_id']
        lecture = Lecture.objects.get(id=lecture_id)
        name = lecture.name
        term = lecture.term
        count = lecture.count
        start_time = lecture.start_time.strftime("%H:%M")
        beacon_major = lecture.room_code.beacon.major
        beacon_minor = lecture.room_code.beacon.minor
        data = {'name':name, 'term':term, 'count':count, 'beacon_major':beacon_major, 'beacon_minor':beacon_minor, 'start_time':start_time}
        serializer_class = LectureSerializer(data)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    
class AttendData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        username = request.user.get_username()
        attend = attendance.objects.filter(username=username)
        serializer_class = AttendSerializer(attend, many=True)
        return Response(serializer_class.data)
    
    def post(self, request):
        username = request.user.get_username()
        ymd = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        # 요청 받은 출석 결과
        result_data = request.data['result']
        lecture_id = request.data['lecture']
        try:
            attend = attendance.objects.filter(time=ymd).filter(lecture_id=lecture_id).get(username=username)

            # 기존의 출석 결과 str->dict
            attend_result = json.loads(attend.result)

            # 기존의 출석 결과 dict로 변경
            result_data = json.loads(result_data)
            attend_result.update(result_data)
            result = json.dumps(attend_result)
            
            edit_data = {'username':attend.username, 'lecture':attend.lecture_id, 'result': result}
            serializer = AttendSerializer(attend, data = edit_data)
            # 직접 유효성 검사
            if serializer.is_valid():
                # 저장
                serializer.save()
                if request.data.get('end') is not None:
                    final_result_function(lecture_id,username,ymd)    
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except ObjectDoesNotExist:
            serializer = AttendSerializer(data=request.data)
            if serializer.is_valid():   # 직접 유효성 검사
                serializer.save()       # 저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Facial_AttendData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        username = request.user.get_username()
        attend = facial_attendance.objects.filter(username=username)
        serializer_class = Facial_AttendSerializer(attend, many=True)
        return Response(serializer_class.data)
    
    def post(self, request):
        username = request.user.get_username()
        ymd = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        # 요청 받은 출석 결과
        result_data = request.data['result']
        lecture_id = request.data['lecture']
        try:
            attend = facial_attendance.objects.filter(time=ymd).filter(lecture_id=lecture_id).get(username=username)

            # 기존의 출석 결과 str->dict
            attend_result = json.loads(attend.result)

            # 기존의 출석 결과 dict로 변경
            result_data = json.loads(result_data)
            attend_result.update(result_data)
            result = json.dumps(attend_result)
            
            edit_data = {'username':attend.username, 'lecture':attend.lecture_id, 'result': result}
            serializer = Facial_AttendSerializer(attend, data = edit_data)
            # 직접 유효성 검사
            if serializer.is_valid():
                # 저장
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except ObjectDoesNotExist:
            serializer = Facial_AttendSerializer(data=request.data)
            if serializer.is_valid():   # 직접 유효성 검사
                serializer.save()       # 저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()


class FinalResultData(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        username = request.user.get_username()
        ymd = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        lecture_id = request.data['lecture']
        lecture = Lecture.objects.get(id=lecture_id)
        try:
            attend = attendance.objects.filter(time=ymd).filter(lecture_id=lecture_id).get(username=username)
            if attend.final_result == "출석":
                final_attend = "○"
            elif attend.final_result == "지각":
                final_attend = "△"
            else:
                final_attend = "X"
            data = {'username':username, 'lecture':lecture.name, 'final_attend':final_attend}
            serializer_class = FinalResultSerializer(data)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogData(APIView): 
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.get_username()
        log = userlog.objects.filter(username=username)
        serializer_class = LogSerializer(log, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        username = request.user.get_username()
        time = request.data['time'] #request time
        check = request.data['check'] # in/out
        lecture = request.data['lecture'] #lecture id

        result = {'username':username, 'time': time, 'check':check, 'lecture':lecture}
        serializer = LogSerializer(data=result)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
