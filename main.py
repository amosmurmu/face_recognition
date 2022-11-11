# importing all necessary modules 
import cv2
import face_recognition

# loading and reading image from path
image = cv2.imread("./known_images/jobs_1.jpg")
image_recog = face_recognition.load_image_file("./known_images/jobs_1.jpg")

# Release handle to the webcam
cv2.imshow('displaying image', image)
cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB)

if cv2.waitKey(0) & 0xFF == ord('q'):
	pass
else:
	pass

# making reference object for webcam
# video_capture = cv2.VideoCapture(0)

# Find all the faces in the image
face_locations = face_recognition.face_locations(image_recog)
# Or maybe find the facial features in the image
face_landmarks_list = face_recognition.face_landmarks(image_recog)

# Or you could get face encodings for each face in the image:
list_of_face_encodings = face_recognition.face_encodings(image_recog)

# video_capture.release()
# print(face_locations)

# face_len = len(face_locations)

# print(face_len)
# for i in face_len:
# 	print(face_locations[i])

cv2.destroyAllWindows()
