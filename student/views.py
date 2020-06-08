from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# from .models import enroll
from attendance.models import attendance
from lecture.models import Lecture
from .models import TakeLectures
from django.core.paginator import Paginator

def student(request):
    # 현재 접속 중인 학생의 학번 추출
    username = request.user.get_username()
    lecture_list = TakeLectures.objects.filter(username=username)

    attends = attendance.objects
    # boards = DjangoBoard.objects
    attend_list = attendance.objects.all().order_by('-id')
    # board_list = DjangoBoard.objects.all().order_by('-id')
    
    # # 게시판 모든 글들을 대상으로 한다.
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
    # return render(request,'student.html',{'lecture_list':lecture_list, 'attends':attends, 'posts':posts,'page_range':page_range,'attend_list':attend_list})
    return render(request,'student.html',{'lecture_list':lecture_list})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'main.html')

