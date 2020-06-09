from django.shortcuts import render
from .recognition import detect_face
from django.contrib.auth.models import User
from student.models import Student
from lecture.models import Lecture
from attendance.models import attendance
from datetime import datetime
from time import strftime, time, localtime
from django.core.exceptions import ObjectDoesNotExist
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
			attend = attendance.objects.filter(time=ymd).get(username=user)
			if numbering[number] > 100:
				attend.result.udpate("{ '" + str(now.hour) + "' : 'ATTEND'}")
			else:
				attend.result.udpate("{ '" + str(now.hour) + "' : 'ABSENT'}")

		except ObjectDoesNotExist:
			user = User.objects.get(username=list(udata.keys())[number])
			if numbering[number] > 100:
				new_post = attendance.objects.create(username=user, lecture=lec1, result="{'" + str(now.hour) + "' : 'ATTEND'}" )
			else:
				new_post = attendance.objects.create(username=user, lecture=lec1, result="{'" + str(now.hour) + "' : 'ATTEND'}" )
	return render(request, "check.html", {'udata':udata.values})















