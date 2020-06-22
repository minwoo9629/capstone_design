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
from django.core.paginator import Paginator
# Create your views here.


def prof(request):
    username = request.user.get_username()
    lecture_list = GiveLectures.objects.filter(username=username)
    return render(request, 'prof.html', {'lecture_list': lecture_list})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')


def detail(request, lecture_id):
    username = request.user.get_username()
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

            lecture_list = GiveLectures.objects.filter(username=username)
            lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
            lecture_in_date = attendance.objects.filter(
                lecture=lecture_detail).filter(time__date=date_obj)

            #attend_list = attendance.objects.filter(lecture=lecture_id).filter(username=username).order_by('-id')

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
        return render(request, 'prof_detail.html', {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'page_range':page_range})

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

    return render(request, 'prof_check.html', {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail':lecture_detail, 'form':form, 'date':date})    
