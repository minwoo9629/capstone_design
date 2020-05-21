from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from lecture.models import GiveLectures, Lecture
from .models import Professor
from attendance.models import attendance
import datetime
from .forms import FindDateForm
# Create your views here.
def prof(request):
    username = request.user.get_username()
    lecture_list = GiveLectures.objects.filter(username=username)
    return render(request,'prof.html', {'lecture_list':lecture_list})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')


def detail(request, lecture_id):
    username = request.user.get_username()
    form = FindDateForm()
    lecture_list = GiveLectures.objects.filter(username=username)
    
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    attends = attendance.objects.filter(lecture=lecture_detail)
    
    return render(request, 'prof_detail.html', {'attends':attends, 'lecture_list':lecture_list, 'lecture_detail':lecture_detail, 'form':form})

def change_date(request):
    if request.method == 'POST':
        form = FindDateForm(request.POST)
