from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count
from lecture.models import GiveLectures, Lecture
from .models import Professor
<<<<<<< HEAD
from attendance.models import attendance, facial_attendance
=======
from attendance.models import attendance,  facial_attendance
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
from datetime import datetime
from .forms import FindDateForm
import json
from itertools import chain
from collections import defaultdict
from time import strftime
from django.core.paginator import Paginator
# Create your views here.

<<<<<<< HEAD

def prof(request):
    username = request.user.get_username()
    lecture_list = GiveLectures.objects.filter(username=username)
    return render(request, 'prof.html', {'lecture_list': lecture_list})

=======
def prof(request):
    username = request.user.get_username()
    group_value = request.user.groups.values()
    # 개설된 강의 중 교수가 가르치는 강의 객체들을 얻음.
    lecture_list = GiveLectures.objects.filter(username=username)
    return render(request,'prof.html',{'lecture_list':lecture_list, 'group':group_value[0]["name"]})
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

<<<<<<< HEAD

def detail(request, lecture_id):
    username = request.user.get_username()
=======
def detail(request, lecture_id):
    username = request.user.get_username()
    group_value = request.user.groups.values()
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
    if not request.method =='POST':
        if 'search-date-post' in request.session:
            request.POST = request.session['search-date-post']
            request.method = 'POST'

    if request.method == 'POST': #날짜 누를 때
        form = FindDateForm(request.POST)
        request.session['search-date-post'] = request.POST
        if form.is_valid:
            
            date = (form.data['find_date'])
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            date_obj = datetime.date(date_obj)

            lecture_list = GiveLectures.objects.filter(username=username)
            lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
            lecture_in_date = attendance.objects.filter(
<<<<<<< HEAD
                lecture=lecture_detail).filter(time=date_obj).order_by('id')

=======
            lecture=lecture_detail).filter(time=date_obj).order_by('id')
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7

            # 해당 수업의 출석들에 대해서 pagination 진행
            num = 5
            paginator = Paginator(lecture_in_date, num)
            # 게시판 객체 num 개를 한 페이지로 자른다.
            attend_page = request.GET.get('page')
            # request된 페이지를 변수에 담는다.
            attends = paginator.get_page(attend_page)
            # request된 페이지를 얻어온 뒤 post에 저장

            page_numbers_range = 5
            #화면에 보여줄 페이지 번호 갯수
            max_index = len(paginator.page_range)
            current_page = int(attend_page) if attend_page else 1
            start_index = int((current_page - 1) /
                              page_numbers_range) * page_numbers_range
            end_index = start_index + page_numbers_range
            if end_index >= max_index:
                end_index = max_index

            page_range = paginator.page_range[start_index:end_index]
<<<<<<< HEAD
        return render(request, 'prof_detail.html', 
        {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'page_range':page_range, 'date':date_obj})
=======
        return render(request, 'prof_detail.html', {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'page_range':page_range,'date':date_obj,'group':group_value[0]["name"]})
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7

    elif request.method == 'GET': #과목 누를 때
            
        form = FindDateForm()
        lecture_list = GiveLectures.objects.filter(username=username)
        lecture_detail = get_object_or_404(Lecture, pk=lecture_id)

<<<<<<< HEAD
        return render(request, 'prof_detail.html', {'lecture_list':lecture_list, 'lecture_detail':lecture_detail, 'form':form})


=======
        return render(request, 'prof_detail.html', {'lecture_list':lecture_list, 'lecture_detail':lecture_detail, 'form':form,'group':group_value[0]["name"]})
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7

def show_detail(request, lecture_id, username, date): #student_id : 학번
    this_lecture = get_object_or_404(Lecture, pk=lecture_id)
    attend = attendance.objects.filter(lecture=this_lecture).filter(time=date).get(username=username)
    facial_attend = facial_attendance.objects.filter(lecture=this_lecture).filter(time=date).get(username=username)

    return render(request, 'prof_check.html', {'attend':attend, 'facial_attend' : facial_attend})

def change_date(request):
    username = request.user.get_username()
    lecture_list = GiveLectures.objects.filter(username=username)

    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    attends = attendance.objects.filter(lecture=lecture_detail)

    if request.method == 'POST':
        form = FindDateForm(request.POST)
        if form.is_valid():
            date = form.data('find_date')

<<<<<<< HEAD
    return render(request, 'prof_check.html', {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'date':date})    
=======
    return render(request, 'prof_check.html', {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'date':date})



>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
