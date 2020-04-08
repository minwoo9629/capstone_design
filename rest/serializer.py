from rest_framework import serializers
from student.models import enroll, Student

class UserLectureSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        now_lecture = serializers.CharField(max_length=20)
        now_room = serializers.CharField(max_length=10)
        now_room_beacon_major = serializers.CharField(max_length=10)
        now_room_beacon_minor = serializers.CharField(max_length=10)
        start_time = serializers.TimeField()
        end_time = serializers.TimeField()

class UserListSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        userface = serializers.ImageField()

class hi(serializers.ModelSerializer):
        class Meta:
                model = enroll
                fields = ['user']