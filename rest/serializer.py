from rest_framework import serializers
from student.models import Student
<<<<<<< HEAD
from attendance.models import attendance, userlog, facial_attendance

class UserLectureSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        lecture = serializers.CharField(max_length=20)
        lecture_code = serializers.CharField(max_length=20)
        room_code = serializers.CharField(max_length=10)
        room_name = serializers.CharField(max_length=10)
        beacon_major = serializers.CharField(max_length=10)
        beacon_minor = serializers.CharField(max_length=10)
        start_time = serializers.TimeField()
        end_time = serializers.TimeField()

=======
from attendance.models import attendance, facial_attendance, userlog

class LectureSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=20)
        term = serializers.CharField(max_length=10)
        count = serializers.IntegerField()
        beacon_major = serializers.CharField(max_length=10)
        beacon_minor = serializers.CharField(max_length=10)
        start_time = serializers.TimeField()


# 현재 수강할 강의가 없는 경우 message 전달
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
class MessageSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        message = serializers.CharField(max_length=30)

class AttendSerializer(serializers.ModelSerializer):
        class Meta:
                model = attendance
                fields = '__all__'

class Facial_AttendSerializer(serializers.ModelSerializer):
        class Meta:
                model = facial_attendance
                fields = '__all__'

class FinalResultSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        lecture = serializers.CharField(max_length=30)
        final_attend = serializers.CharField(max_length=10)

class LogSerializer(serializers.ModelSerializer):
        class Meta:
                model = userlog
                fields = '__all__'

<<<<<<< HEAD
        
=======

>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
