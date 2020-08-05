#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count
from lecture.models import GiveLectures, Lecture
from .models import Professor
from attendance.models import attendance,  facial_attendance
from datetime import datetime
from .forms import FindDateForm
import json
from itertools import chain
from collections import defaultdict
from time import strftime
from django.core.paginator import Paginator

# 엑셀파일 다운로드 구현
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
from django.http import HttpResponse
import sys
import mimetypes
import urllib
# Create your views here.


def prof(request):
    username = request.user.get_username()
    group_value = request.user.groups.values()
    # 개설된 강의 중 교수가 가르치는 강의 객체들을 얻음.
    lecture_list = GiveLectures.objects.filter(username=username)
    context = {'lecture_list': lecture_list, 'group': group_value[0]["name"]}
    return render(request, 'prof.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')


def detail(request, lecture_id):
    username = request.user.get_username()
    group_value = request.user.groups.values()
    #출석률
    # progress_value = attend_progress(lecture_id)
    date_queryset = attendance.objects.filter(lecture=lecture_id).values('time').distinct().order_by('time')
    dates = []
    for date in date_queryset:
        dates.append(str(date['time']))

    if request.method == 'POST':  # 날짜 누를 때
        date_obj = request.POST['date']

        lecture_list = GiveLectures.objects.filter(username=username)
        lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
        lecture_in_date = attendance.objects.filter(lecture=lecture_detail).filter(time=date_obj).order_by('id')

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
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        
        context = {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail': lecture_detail,'page_range': page_range, 'date': date_obj, 'group': group_value[0]["name"], 'dates': dates}
        return render(request, 'prof_detail.html', context)

    elif request.method == 'GET':  # 과목 누를 때

        lecture_list = GiveLectures.objects.filter(username=username)
        lecture_detail = get_object_or_404(Lecture, pk=lecture_id)

        context = {'lecture_list': lecture_list, 'lecture_detail': lecture_detail, 'group': group_value[0]["name"], 'dates': dates}
        return render(request, 'prof_detail.html', context)


def show_detail(request, lecture_id, username, date):  # student_id : 학번
    this_lecture = get_object_or_404(Lecture, pk=lecture_id)
    attend = attendance.objects.filter(lecture=this_lecture).filter(time=date).get(username=username)
    facial_attend = facial_attendance.objects.filter(lecture=this_lecture).filter(time=date).get(username=username)
    
    context = {'attend': attend, 'facial_attend': facial_attend}
    return render(request, 'prof_check.html', context)


def change_date(request):
    username = request.user.get_username()
    lecture_list = GiveLectures.objects.filter(username=username)

    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    attends = attendance.objects.filter(lecture=lecture_detail)

    if request.method == 'POST':
        form = FindDateForm(request.POST)
        if form.is_valid():
            date = form.data('find_date')
    
    context = {'attends': attends, 'lecture_list': lecture_list, 'lecture_detail': lecture_detail, 'form': form, 'date': date}
    return render(request, 'prof_check.html', context)


# 엑셀파일 다운 구현
def download(request, lecture_id):
    if request.method == "GET":
        lecture_obj = get_object_or_404(Lecture, pk=lecture_id)
        time_obj = attendance.objects.filter(
            lecture=lecture_id).values('time').distinct()
        wb = Workbook()
        sheet = wb.active
        for index in time_obj:
            if time_obj[0] == index:
                sheet.title = str(index['time'])
                time_attend = attendance.objects.filter(
                    lecture=lecture_id).filter(time=index['time'])
            else:
                ws = wb.create_sheet(str(index['time']))

        filename = lecture_obj.name + ".xlsx"
        file_name = urllib.parse.quote(filename.encode('utf-8'))
        response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'%s' % file_name
        return response


#출석률
# def attend_progress(lecture_id):
#     attend_queryset = attendance.objects.filter(lecture=lecture_id).order_by('-id')
#     if not attend_queryset:
#         progress_value = '출석 값이 없습니다.'
#     else:
#         if attend_queryset[0].final_result == '처리중':
#             progress_value = '출석이 집계 준비중 입니다.'
#         else:
#             # 전체 출석 횟수
#             all_attend_value = len(attend_queryset)
#             # 출석 횟수
#             attend_value = len(attend_queryset.filter(final_result='출석'))
#             n = (attend_value/all_attend_value)*100
#             progress_value = round(n)
#     return progress_value
