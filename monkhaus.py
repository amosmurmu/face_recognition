import face_recognition
from PIL import Image, ImageDraw
import cv2
import os
import glob 
from datetime import datetime

known_dir = glob.glob('known_images/*.jpg')
unknown_dir = glob.glob('unknown_images/*.jpg')

known_names =[]
encoding_list =[]

for img in known_dir:

	image = face_recognition.load_image_file(img)

	face_encoding = face_recognition.face_encodings(image)[0]
	encoding_list.append(face_encoding)
	print(img)
	known_names.append(img)
	
print(known_names)
	
for unknownimg in unknown_dir:
	unknown_img = face_recognition.load_image_file(unknownimg)
	unknown_encoding = face_recognition.face_encodings(unknown_img)[0]
	
	for img in known_dir :

		image = face_recognition.load_image_file(img)
	
	
		# print(unknown_encoding)
		result = face_recognition.compare_faces(encoding_list,unknown_encoding)
		print(result)
		if True in result:

			known_face_locations = face_recognition.face_locations(image)
			known_features = face_recognition.face_landmarks(image)
			
			# using PIL python imaging library for drawing
			pil_image = Image.fromarray(image)
			draw = ImageDraw.Draw(pil_image)

			# using open cv to display face image 
			image_cv= cv2.imread(img)
			cv2.cvtColor( src = image_cv, code = cv2.COLOR_BGR2RGB)

			
			# LOCATION OF FACES 
			def func_face_loc():
					# face location for specific location
					#top right bottom left
					#y1	  x2   y2	  x1	
					known_face_location = known_face_locations[0]
					x1=known_face_location[3]
					y1=known_face_location[0]
					x2=known_face_location[1]
					y2=known_face_location[2]

					draw.rounded_rectangle((x1,y1,x2,y2), outline="red",width=5,radius=10)
					cv2.rectangle(image_cv,(x1,y1),(x2,y2), color=(0,0,255), thickness=4)
					# cv2.putText(image_cv, name ,(x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,(255,255,255),2)
				

			# FEATURES OF FACES
			def func_features_face():

				my_dict= known_features[0]
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

			func_face_loc()
			func_features_face()
			func_display_results()

	
		else :
			print("face not recognized")
		break

# def markAttendance(name):
#     with open('Attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             time = now.strftime('%I:%M:%S:%p')
#             date = now.strftime('%d-%B-%Y')
#             f.writelines(f'n{name}, {time}, {date}')


