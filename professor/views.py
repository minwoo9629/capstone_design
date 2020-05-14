from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from lecture.models import GiveLectures
from .models import Professor
# Create your views here.
def prof(request):
    username = request.user.get_username()
    
    # 개설된 강의 중 교수가 가르치는 강의 객체들을 얻음.
    lecture_list = GiveLectures.objects.filter(username=username)
    return render(request,'prof.html',{'lecture_list':lecture_list})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

def detail(request, lecture_code):
    lecture_detail = get_object_or_404(Lecture, code=lecture_code)
    return render(request, 'detail.html',{'lecture_detail':lecture_detail})


