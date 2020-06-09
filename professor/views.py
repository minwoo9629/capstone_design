from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count
from lecture.models import GiveLectures, Lecture
from .models import Professor
from attendance.models import attendance
from datetime import datetime
from .forms import FindDateForm
import json
from itertools import chain
from collections import defaultdict
from time import strftime
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
    if request.method == 'POST': #날짜 누를 때
        form = FindDateForm(request.POST)
        if form.is_valid:
            
            date = (form.data['find_date'])
            date_obj = datetime.strptime(date, '%Y-%m-%d')

            lecture_list = GiveLectures.objects.filter(username=username)
            lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
            lecture_in_date = attendance.objects.filter(lecture=lecture_detail).filter(time__date=date_obj)
            
        return render(request, 'prof_detail.html', {'attends':lecture_in_date, 'lecture_list':lecture_list, 'lecture_detail':lecture_detail, 'form':form})


    elif request.method == 'GET': #과목 누를 때
        form = FindDateForm()
        lecture_list = GiveLectures.objects.filter(username=username)
        lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
       
        return render(request, 'prof_detail.html', {'lecture_list':lecture_list, 'lecture_detail':lecture_detail, 'form':form})

def change_date(request):
    username = request.user.get_username()
    lecture_list = GiveLectures.objects.filter(username=username)
    
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    attends = attendance.objects.filter(lecture=lecture_detail)

    if request.method == 'POST':
        form = FindDateForm(request.POST)
        if form.is_valid():
            date = form.data('find_date')
        
    return render(request, 'prof_check.html', {'attends':attends, 'lecture_list':lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'date':date})    