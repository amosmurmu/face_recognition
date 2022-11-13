import face_recognition
from PIL import Image, ImageDraw
import cv2
import os
from datetime import datetime

jobs_img = face_recognition.load_image_file("known_images/jobs.jpg")
virat_img = face_recognition.load_image_file("known_images/virat_kohli.jpg")
indian_img = face_recognition.load_image_file("known_images/Indian_team.jpg")
# face locations
jobs_face_loc = face_recognition.face_locations(jobs_img)
virat_face_loc = face_recognition.face_locations(virat_img)
team_list = face_recognition.face_locations(indian_img)
# face landmarks / features 
jobs_face_list = face_recognition.face_landmarks(jobs_img)
virat_face_list = face_recognition.face_landmarks(virat_img)

# face encodings 
try:
	jobs_encoding = face_recognition.face_encodings(jobs_img)
	virat_encoding = face_recognition.face_encodings(virat_img)
except IndexError:
		print("no face found")

unknown_img = face_recognition.load_image_file("unknown_images/virat_kohli.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_img)

known_faces_loc = []
known_faces_list = []
known_faces_encodings = []

# creating list of known faces 
known_faces_loc = [jobs_face_loc,virat_face_loc]
known_faces_list = [jobs_face_list,virat_face_list]
known_faces_encodings = [jobs_encoding,virat_encoding]


# known_faces_loc = face_recognition.face_locations(img)
# known_faces_list = face_recognition.face_landmarks(img)
# known_faces_encodings = face_recognition.face_encodings(img)
# using PIL python imaging library for drawing
pil_image = Image.fromarray(jobs_img)
draw = ImageDraw.Draw(pil_image)

# using open cv to display face image 
image_cv= cv2.imread("known_images/jobs.jpg")
cv2.cvtColor( src = image_cv, code = cv2.COLOR_BGR2RGB)

# LOCATION OF FACES 
def func_face_loc():
	for face in known_faces_loc:
		# face location for specific location
		#top right bottom left
		#y1	  x2   y2	  x1	
		known_face_location = face[0]
		x1=known_face_location[3]
		y1=known_face_location[0]
		x2=known_face_location[1]
		y2=known_face_location[2]

		draw.rounded_rectangle((x1,y1,x2,y2), outline="red",width=5,radius=10)
		cv2.rectangle(image_cv,(x1,y1),(x2,y2), color=(0,0,255), thickness=4)
		# cv2.putText(image_cv, name ,(x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,(255,255,255),2)
		break

# FEATURES OF FACES
def func_features_face():
	for known_faces in known_faces_list :

		my_dict= known_faces[0]
		# facial landmarks or features
		for features in my_dict.values():
			# print(features)
			draw.line((features),width=2)

			first = 0 
			next_value = 1
			len_list = len(features)
			value = 0
			while(value < len_list-1):

				# print(first,next_value)
				# print(features[first],features[next_value])
				cv2.line(image_cv,features[first],features[next_value],color=(255,0,0),thickness=1)
				value+=1
				first+=1
				next_value+=1
		break

# comparing the face encodings
def func_comparing():
	for known_encoding in known_faces_encodings:
		# print(known_encoding[0])
		ret = face_recognition.compare_faces(known_encoding[0],unknown_encoding)
		print(ret)
		

# Displaying the results
def func_display_results():
	#Displaying the results 
	pil_image.show()
	cv2.imshow('Display_Window',image_cv)

	if cv2.waitKey(0) & 0xFF == ord('q'):
		pass
	else:
		pass
	cv2.destroyAllWindows()

func_comparing()
func_face_loc()
func_features_face()
func_display_results()
	# markAttendance(name)
		
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'n{name}, {time}, {date}')


