import face_recognition

image = face_recognition.load_image_file("./known_images/jobs_1.jpg")


# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

# Or maybe find the facial features in the image
face_landmarks_list = face_recognition.face_landmarks(image)

# Or you could get face encodings for each face in the image:
list_of_face_encodings = face_recognition.face_encodings(image)



print(face_locations)