from django.shortcuts import render
from .recognition import detect_face
from django.contrib.auth.models import User
from student.models import Student
from lecture.models import Lecture
from attendance.models import Attendance, facial_attendance
from datetime import datetime
from time import strftime, time, localtime
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.

def recognition(request):
	lec1 = Lecture.objects.get(code='L001')
	student_data = Student.objects.all()
	udata = {}
	for data in student_data:
		udata[data.username] = str(data.photo)

	numbering = detect_face(udata, lec1)
	now = datetime.now()
	ymd = strftime('%Y-%m-%d',localtime(time()))
	for number in range(len(numbering)):
		#print(list(udata.keys())[number])
		try:
			user = User.objects.get(username=list(udata.keys())[number])
			attend = Attendance.objects.filter(time=ymd).filter(lecture=lec1).get(username=user)
			attend_result = json.loads(attend.result)

			if numbering[number] > 100:
				d = json.loads('{"' + str(now.hour + 1) + '" : "ATTEND"}')
				
			else:
				d = json.loads('{"' + str(now.hour + 1) + '" : "ABSENT"}')
			
			attend_result.update(d)
			result = json.dumps(attend_result)
			attend.result = result
			attend.save()
			print("1234")
		except ObjectDoesNotExist:
			user = User.objects.get(username=list(udata.keys())[number])
			if numbering[number] > 100:
				new_post = facial_attendance.objects.create(username=user, lecture=lec1, result='{"' + str(now.hour) + '" : "ATTEND"}' )
			else:
				new_post = facial_attendance.objects.create(username=user, lecture=lec1, result='{"' + str(now.hour) + '" : "ABSENT"}' )
	return render(request, "check.html", {'udata':udata.values})















