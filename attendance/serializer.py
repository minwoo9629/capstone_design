from rest_framework import serializers
from .models import attendance

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ['user','lecture_code','result','time']