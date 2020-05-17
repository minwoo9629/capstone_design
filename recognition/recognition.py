import face_recognition
import cv2
from django.conf import settings
from attendance.models import attendance
from student.models import Student
from django.contrib.auth.models import User
from lecture.models import Lecture

def detect_face(**user_data):
	#user_data = User.objects.filter(groups__name="student")
	video_path = "media/video/"
	lect = Lecture.objects.get(lecture_code="L001")
	input_movie = cv2.VideoCapture(video_path+"untitled.mp4")
	length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
	names = []
	encodings = []
	
	for key in user_data.keys():
		names.append(key)
		image_path = "media/" + user_data[key]
		image = face_recognition.load_image_file(image_path)
		encodings.append(face_recognition.face_encodings(image)[0])
	
	
	numbering = [0 for _ in range(len(names))]
	
	face_locations = []
	face_encodings = []
	frame_number = 0
	
	while True:
		ret, frame = input_movie.read()
		frame_number += 1
		if not ret:
			break
		rgb_frame = frame[:, :, ::-1]
		face_locations = face_recognition.face_locations(rgb_frame)
		face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

		for face_encoding in face_encodings:
			matchs = face_recognition.compare_faces(encodings, face_encoding, tolerance=0.45)
			check_point = 0
			for match in matchs:
				if match: 
					numbering[check_point] += 1
				check_point += 1
			
	
		print("Writing frame {} / {}".format(frame_number, length))

		for number in range(len(numbering)):
		#print(names[number], numbering[number])
			if numbering[number] > 100:
				user = User.objects.get(username=names[number])
				new_post = attendance.objects.create(user=user, lecture_code=lect, result="ATTEND" )
			else:
				user = User.objects.get(username=names[number])
				new_post = attendance.objects.create(user=user, lecture_code=lect, result="ABSENT" )


		
	for determine_number in numbering:
		if determine_number > 100:
			#n = attendance.objects.create(User="20150001", Lecture_code="L001", Result='attend')
			print('OK')


		else:
			print('Not OK')
	

	input_movie.release()
	cv2.destroyAllWindows()
	
