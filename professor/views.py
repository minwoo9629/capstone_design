from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from lecture.models import Lecture
from .models import Professor
# Create your views here.
def prof(request):
    username = request.user.get_username()
    prof_code = Professor.objects.get(user__username=username).prof_code
    lecture_list = Lecture.objects.filter(prof_code=prof_code)
    return render(request,'prof.html',{'lecture_list':lecture_list})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

def detail(request, lecture_code):
    lecture_detail = get_object_or_404(Lecture, lecture_code=lecture_code)
    return render(request, 'detail.html',{'lecture_detail':lecture_detail})


