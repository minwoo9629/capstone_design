from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import enroll
from attendance.models import attendance
from lecture.models import Lecture
# Create your views here.
def student(request):
    username = request.user.get_username()
    enrolls = enroll.objects.get(user__username=username)
    return render(request,'student.html',{'enrolls':enrolls})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

def attend(request):
    if request.method == 'POST':
        username = request.user.get_username()
        me = User.objects.all()
        lect = Lecture.objects.get(lecture_code="L012")
        for aa in me:
            new_post = attendance.objects.create(user=aa,lecture_code=lect,result="ATTEND")
        # dd = attendance.objects.all()
        # dd.update(result="LATE")
        return redirect('student')
    return render(request, 'student.html')

