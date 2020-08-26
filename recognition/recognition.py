import face_recognition
import cv2
from django.conf import settings
from attendance.models import attendance
from student.models import Student
from django.contrib.auth.models import User
from lecture.models import Lecture
from attendance.models import facial_attendance
from time import strftime,time, localtime
from django.core.exceptions import ObjectDoesNotExist
import json
def detect_face(user_data, lec, key):
	
	video_path = "http://203.230.103.202:59551/videostream.cgi?user=admin&pwd=isl7528727"
	input_movie = cv2.VideoCapture(video_path)
	#오늘 날짜
	ymd = strftime('%Y-%m-%d',localtime(time()))

	height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
	width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
	frame = int(input_movie.get(cv2.CAP_PROP_FPS))
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	output_movie = cv2.VideoWriter('media/video/'+ymd+' ' + str(lec)+ '.avi', fourcc, frame, (width, height))
	# names = []
	# encodings = []
	
	name = user_data.username
	image_path = 'media/' + str(user_data.photo)
	image = face_recognition.load_image_file(image_path)
	encoding = face_recognition.face_encodings(image)[0]

	# for key in user_data:
	# 	names.append(key)
	# 	image_path = "media/" + user_data[key]
	# 	image = face_recognition.load_image_file(image_path)
	# 	encodings.append(face_recognition.face_encodings(image)[0])
	
	#numbering = [0 for _ in range(len(names))]
	face_locations = []
	face_encodings = []
	face_names = []
	frame_number = 0
	limit_frame = 200
	numbering = 0
	while frame_number < limit_frame:
		ret, frame = input_movie.read()
		frame_number += 1
		if not ret:
			break
		rgb_frame = frame[:, :, ::-1]
		face_locations = face_recognition.face_locations(rgb_frame)
		face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
		
		if cv2.waitKey(1) & 0xff == ord('q'):
			break


		for face_encoding in face_encodings:
			match = face_recognition.compare_faces([encoding], face_encoding, tolerance=0.45)
			if match:
				numbering += 1
				face_names.append(name)
			# check_point = 0
			# for match in matchs:
			# 	if match: 
			# 		numbering[check_point] += 1
			# 		face_names.append(names[check_point])
			# 	check_point += 1
			
	
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			if not name:
				continue
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

		#cv2.imshow('IP camera', frame)
		print("Writing frame {} / {}".format(frame_number, limit_frame))
		output_movie.write(frame)
		print(numbering)


	# for number in range(len(numbering)):
	# #print(names[number], numbering[number])
	# 	if numbering[number] > 100:
	# 		user = User.objects.get(username=names[number])
	# 		new_post = attendance.objects.create(username=user, lecture=lec1, result="{'09:00' : 'ATTEND'}" )
			
		
	input_movie.release()
	output_movie.release()
	cv2.destroyAllWindows()
	username = user_data.username
	
	try:
		attend = facial_attendance.objects.filter(time=ymd).filter(lecture=lec).get(username=username)
		attend_result = json.loads(attend.result)

		if numbering > 100:
			a = json.loads('{"' + str(key[0]) +  '" : "ATTEND"}')
		else:
			a = json.loads('{"' + str(key[0]) + '" : "ABSENT"}')
		attend_result.update(a)
		result = json.dumps(attend_result)
		attend.result = result
		attend.save()

	except ObjectDoesNotExist:
		suup = Lecture.objects.get(id=lec)
		if numbering > 100:
			facial_attendance.objects.create(username=username, lecture=suup, result='{"' + str(key[0])  + '" : "ATTEND"}')
		else:
			facial_attendance.objects.create(username=username, lecture=suup, result='{"' + str(key[0])  + '" : "ABSENT"}')