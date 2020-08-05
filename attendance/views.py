from django.shortcuts import render
from django.shortcuts import render
from .models import attendance, facial_attendance
from lecture.models import Lecture
import json

def detail(request, lecture_id, attend_time):
    username = request.user.get_username()
    attend = attendance.objects.filter(lecture=lecture_id).filter(time=attend_time).get(username=username)
    facial_attend = facial_attendance.objects.filter(lecture=lecture_id).filter(time=attend_time).get(username=username)
    count = attend.lecture.count
    attend_list = list(json.loads(attend.result).values())
    facial_attend_list = list(json.loads(facial_attend.result).values())
    return render(request,'attend_detail.html',{'attend':attend_list, 'facial_attend':facial_attend_list, "count":count})



