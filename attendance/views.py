from django.shortcuts import render
from rest_framework import viewsets
from .models import attendance
from .serializer import AttendSerializer

class AttendViewSet(viewsets.ModelViewSet):

    queryset = attendance.objects.all()
    serializer_class = AttendSerializer
