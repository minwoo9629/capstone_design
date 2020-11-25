import face_recognition
import cv2
from django.conf import settings
from attendance.models import Attendance
from student.models import Student
from django.contrib.auth.models import User
from lecture.models import Lecture
from attendance.models import facial_attendance
from time import strftime,time, localtime
from django.core.exceptions import ObjectDoesNotExist
import json
import os
"""
1명의 출석 과정에서 그 학생의 얼굴 사진과 IP 카메라에서 들어오는 영상에서 보이는 얼굴의 대조 함수
특정 프레임 이상 나타났을 때 DB로 데이터 전송
"""
def detect_face(user_data, lec, key):
	this_lecture = Lecture.objects.get(id=lec)
	video_path = "your_camera_IP_here"
	input_movie = cv2.VideoCapture(video_path)
	#오늘 날짜
	ymd = strftime('%Y-%m-%d',localtime(time()))
	name = str(user_data.username)
	height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
	width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
	frame = int(input_movie.get(cv2.CAP_PROP_FPS))
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	video_file_path = 'media/hanbat/video/' + ymd + '/' + this_lecture.name + "/" + str(lec[-1]) + '/'
	try:
		if not os.path.isdir(video_file_path):
			os.makedirs(os.path.join(video_file_path))
	except OSError:
		if OSError.errno != errno.EEXIST:
			print("Failed to create directory")
			raise
	output_movie = cv2.VideoWriter(video_file_path +  name + '.avi', fourcc, frame, (width, height))
	# names = []
	# encodings = []
	
	
	image_path = 'media/' + str(user_data.photo)
	image = face_recognition.load_image_file(image_path)
	encoding = face_recognition.face_encodings(image)[0]
	#test_image = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
	#cv2.imshow('a', test_image)
	
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
			match = face_recognition.compare_faces([encoding], face_encoding, tolerance=0.4)
			print(match)
			if match[0]:
				numbering += 1
				face_names.append(name)
			else:
				face_names.append('   ')
			# check_point = 0
			# for match in matchs:
			# 	if match: 
			# 		numbering[check_point] += 1
			# 		face_names.append(names[check_point])
			# 	check_point += 1
			
	
		for (top, right, bottom, left), uname in zip(face_locations, face_names):
			if not uname:
				continue
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			
		cv2.imshow('IP camera', frame)
		print("Writing frame {} / {}".format(frame_number, limit_frame))
		output_movie.write(frame)
		print("now : " + str(numbering))


	# for number in range(len(numbering)):
	# #print(names[number], numbering[number])
	# 	if numbering[number] > 100:
	# 		user = User.objects.get(username=names[number])
	# 		new_post = attendance.objects.create(username=user, lecture=lec1, result="{'09:00' : 'ATTEND'}" )
			
		
	input_movie.release()
	output_movie.release()
	cv2.destroyAllWindows()
	username = user_data.username

	#rest로 들어오는 시간값으로 얼굴인식 테이블에 칼럼 생성
	try:	
		attend = facial_attendance.objects.filter(time=ymd).filter(lecture_id=lec).get(username=username)
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

"""
테스트를 위해 작성한 함수
recognition view로 데이터 return
"""
def test_detect(user_data, lec, key):
	this_lecture = Lecture.objects.get(id=lec)
	video_path = "http://203.230.103.202:59551/videostream.cgi?user=admin&pwd=isl7528727"
	input_movie = cv2.VideoCapture(video_path)
	#오늘 날짜
	ymd = strftime('%Y-%m-%d',localtime(time()))
	#name = str(user_data.username)
	height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
	width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
	frame = int(input_movie.get(cv2.CAP_PROP_FPS))
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	video_file_path = 'media/hanbat/video/' + ymd + '/' + this_lecture.name + "/" 
	try:
		if not os.path.isdir(video_file_path):
			os.makedirs(os.path.join(video_file_path))
	except OSError:
		if OSError.errno != errno.EEXIST:
			print("Failed to create directory")
			raise
	output_movie = cv2.VideoWriter(video_file_path + str(key[0]) +'.mp4', fourcc, frame, (width, height))
	names = []
	encodings = []
	
	
	# image_path = 'media/' + str(user_data.photo)
	# image = face_recognition.load_image_file(image_path)
	# encoding = face_recognition.face_encodings(image)[0]
	#test_image = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
	#cv2.imshow('a', test_image)
	
	for key in user_data:
		names.append(key)
		image_path = "media/" + user_data[key]
		image = face_recognition.load_image_file(image_path)
		encodings.append(face_recognition.face_encodings(image)[0])
	
	numbering = [0 for _ in range(len(names))]
	face_locations = []
	face_encodings = []
	face_names = []
	frame_number = 0
	limit_frame = 200
	#numbering = 0
	while frame_number < limit_frame:
		ret, frame = input_movie.read()
		frame_number += 1
		if not ret:
			break
		rgb_frame = frame[:, :, ::-1]
		face_locations = face_recognition.face_locations(rgb_frame)
		face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
		
		if cv2.waitKey(5) & 0xff == ord('q'):
			break


		for face_encoding in face_encodings:
			matchs= face_recognition.compare_faces(encodings, face_encoding, tolerance=0.4)
			#print(match)
			# if match[0]:
			# 	numbering += 1
			# 	face_names.append(name)
			# else:
			# 	face_names.append('   ')
			check_point = 0
			for match in matchs:
				if match: 
					numbering[check_point] += 1
					face_names.append(names[check_point])
				check_point += 1
			
	
		for (top, right, bottom, left), uname in zip(face_locations, face_names):
			if not uname:
				continue
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			#cv2.putText(frame, uname, (left, bottom), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
		cv2.imshow('IP camera', frame)
		print("Writing frame {} / {}".format(frame_number, limit_frame))
		output_movie.write(frame)
		print("now : " + str(numbering))


	# for number in range(len(numbering)):
	# #print(names[number], numbering[number])
	# 	if numbering[number] > 100:
	# 		user = User.objects.get(username=names[number])
	# 		new_post = attendance.objects.create(username=user, lecture=lec1, result="{'09:00' : 'ATTEND'}" )
			
		
	input_movie.release()
	output_movie.release()
	cv2.destroyAllWindows()
	return numbering
	#username = user_data.username
	# for i in range(len(names)):
	# 	print(i)
		
	# 	try:
	# 		name = names[i]
	# 		username = User.objects.get(username=name)
	# 		#username = username.username
	# 		print(type(username))
	# 		print(username)
	# 		number = numbering[i]
	# 		attend = facial_attendance.objects.filter(time=ymd).filter(lecture_id=lec).get(username=username)
	# 		print(attend)
	# 		attend_result = json.loads(attend.result)

	# 		if number > 100:
	# 			a = json.loads('{"' + str(key[0]) +  '" : "ATTEND"}')
	# 		else:
	# 			a = json.loads('{"' + str(key[0]) + '" : "ABSENT"}')
	# 		attend_result.update(a)
	# 		result = json.dumps(attend_result)
	# 		attend.result = result
	# 		attend.save()

	# 	except ObjectDoesNotExist:
	# 		suup = Lecture.objects.get(id=lec)
	# 		username = User.objects.get(username=name)
	# 		#print(username)
	# 		if number > 100:
	# 			facial_attendance.objects.create(username=username, lecture=suup, result='{"' + str(key[0])  + '" : "ATTEND"}')
	# 		else:
	# 			facial_attendance.objects.create(username=username, lecture=suup, result='{"' + str(key[0])  + '" : "ABSENT"}')
