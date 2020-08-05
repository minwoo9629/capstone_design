from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from attendance.models import attendance
from lecture.models import Lecture
from .models import TakeLectures
from django.core.paginator import Paginator
from datetime import datetime
from time import strftime
from django.core.exceptions import ObjectDoesNotExist


def student(request):
    # 현재 접속 중인 학생의 학번 추출
    username = request.user.get_username()
    group_value = request.user.groups.values()
    lecture_list = TakeLectures.objects.filter(username=username)
    return render(request, 'student.html', {'lecture_list': lecture_list, 'group': group_value[0]["name"]})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')


def detail(request, lecture_id):

    username = request.user.username
    group_value = request.user.groups.values()
    date_queryset = attendance.objects.filter(lecture=lecture_id).filter(username=username).values('time').distinct().order_by('time')
    dates = []
    for date in date_queryset:
        dates.append(str(date['time']))

    progress_value = attend_progress(lecture_id, username)

    if request.method == 'GET':

        lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
        lecture = Lecture.objects.get(id=lecture_id)
        lecture_list = TakeLectures.objects.filter(username=username)
        attend_list = attendance.objects.filter(lecture=lecture_id).filter(username=username).order_by('-id')
        # 해당 수업의 출석들에 대해서 pagination 진행
        num = 5
        paginator = Paginator(attend_list, num)
        # 게시판 객체 num 개를 한 페이지로 자른다.
        attend_page = request.GET.get('page')
        # request된 페이지를 변수에 담는다.
        posts = paginator.get_page(attend_page)
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

        context = {'lecture_list': lecture_list, 'lecture': lecture,
                   'group': group_value[0]["name"], 'posts': posts, 'page_range': page_range, 'attend_list': attend_list, 'dates': dates, 'progress_value':progress_value}
        return render(request, 'student_detail.html', context)

    if request.method == 'POST':  # 날짜 누를 때

        lecture = Lecture.objects.get(id=lecture_id)
        lecture_list = TakeLectures.objects.filter(username=username)
        date = request.POST['date']
        # 날짜에 맞는 출석 객체
        select_attend = attendance.objects.filter(username=username).filter(lecture=lecture_id).filter(time=request.POST['date'])

        context = {'lecture_list': lecture_list, 'lecture': lecture,'group': group_value[0]["name"], 'dates': dates, 'posts': select_attend, 'progress_value':progress_value}
        return render(request, 'student_detail.html', context)


def attend_progress(lecture_id, username):
    attend_queryset = attendance.objects.filter(lecture=lecture_id).filter(username=username).order_by('-id')
    if not attend_queryset:
        progress_value = '출석 값이 없습니다.'
    else:
        if attend_queryset[0].final_result == '처리중':
            progress_value = '출석이 집계 준비중 입니다.'
        else:
            # 전체 출석 횟수
            all_attend_value = len(attend_queryset)
            # 출석 횟수
            attend_value = len(attend_queryset.filter(final_result='출석'))
            n = (attend_value/all_attend_value)*100
            progress_value = round(n)
    return progress_value