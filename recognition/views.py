from django.shortcuts import render
from .recognition import detect_face, test_detect
from django.contrib.auth.models import User
from student.models import Student
from lecture.models import Lecture
from attendance.models import Attendance, facial_attendance
from datetime import datetime
from time import strftime, time, localtime
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.


	"""
	detect_face(udata, lec1, ['09:00']) 리스트는 json 키값 임의로 배정해서 넣음
	테스트를 위해 만든 함수
	실제로 작동되는 함수는 recogniiton.py의 detect_face 
	"""
def recognition(request):
	lec1 = '1'
	student_data = Student.objects.all()
	udata = {}
	for data in student_data:
		udata[data.username] = str(data.photo)

	numbering = test_detect(udata, lec1, ['11:00'])
	print(numbering)
	now = datetime.now()
	ymd = strftime('%Y-%m-%d',localtime(time()))
	for number in range(len(numbering)):
		#print(list(udata.keys())[number])
		try:
			user = User.objects.get(username=list(udata.keys())[number])
			attend = facial_attendance.objects.filter(time=ymd).filter(lecture_id=lec1).get(username=user)
			attend_result = json.loads(attend.result)

			if numbering[number] > 100:
				d = json.loads('{"' + '11:00' + '" : "ATTEND"}')
				
			else:
				d = json.loads('{"' + '11:00' + '" : "ABSENT"}')
			
			attend_result.update(d)
			result = json.dumps(attend_result)
			attend.result = result
			attend.save()
			#print("1234")
		except ObjectDoesNotExist:
			user = User.objects.get(username=list(udata.keys())[number])
			lec = Lecture.objects.get(id=lec1)
			if numbering[number] > 100:
				new_post = facial_attendance.objects.create(username=user, lecture=lec, result='{"' + '11:00' + '" : "ATTEND"}' )
			else:
				new_post = facial_attendance.objects.create(username=user, lecture=lec, result='{"' + '11:00' + '" : "ABSENT"}' )
	return render(request, "check.html", {'udata':udata.values})















