from rest_framework import serializers
from student.models import Student
from attendance.models import attendance

class LectureSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=20)
        term = serializers.CharField(max_length=10)
        count = serializers.IntegerField()
        beacon_major = serializers.CharField(max_length=10)
        beacon_minor = serializers.CharField(max_length=10)
        start_time = serializers.TimeField()


# 현재 수강할 강의가 없는 경우 message 전달
class MessageSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        message = serializers.CharField(max_length=30)

class AttendSerializer(serializers.ModelSerializer):
        class Meta:
                model = attendance
                fields = '__all__'
