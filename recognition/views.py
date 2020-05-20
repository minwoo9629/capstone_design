from django.shortcuts import render
from .recognition import detect_face
from django.contrib.auth.models import User
from student.models import Student
from lecture.models import Lecture
from attendance.models import attendance
import datetime

# Create your views here.

def recognition(request):
	student_data = Student.objects.all()
	udata = {}
	for a in student_data:
#		udata = {a.user.username:a.user.student.photo}
		udata[a.user.username] = str(a.user.student.photo)
#	image = a.user.student.photo
	#print(udata)
	#print(image)
	#detect_face(**udata)
	return render(request, "check.html")
	#return None
