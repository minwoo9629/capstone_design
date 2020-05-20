from rest_framework import serializers
from student.models import Student
from attendance.models import attendance

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

class MessageSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        message = serializers.CharField(max_length=30)

class AttendSerializer(serializers.Serializer):
        class Meta:
                model = attendance
                field = '__all__'