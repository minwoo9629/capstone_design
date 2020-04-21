from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# from .models import enroll
from attendance.models import attendance
from lecture.models import Lecture

def student(request):
    # 현재 접속 중인 학생의 학번 추출
    username = request.user.get_username()
    attend = attendance.objects.get(username=username)
    return render(request,'student.html',{'attend':attend})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

