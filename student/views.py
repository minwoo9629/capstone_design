from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
#from .models import enroll
from attendance.models import attendance
from lecture.models import Lecture
# Create your views here.
def student(request):
    username = request.user.get_username()
    return render(request,'student.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

