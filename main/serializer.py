from django.contrib.auth.models import User
from student.models import enroll
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = enroll
        fields = ['user','get_lecture_list']