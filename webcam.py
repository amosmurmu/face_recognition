import face_recognition
import cv2

# Capture From Web Cam
cap = cv2.VideoCapture(0)

# If want to use video, replace 0 with video path.
# cap = cv2.VideoCapture(VIDEO_PATH)

while True:
    # Get frame from cap
    _, image = cap.read()

    # Find all the faces in the image using the default HOG-based model.
    face_locations = face_recognition.face_locations(image)

    print("Found {} faces in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        
        # We can draw rectangle using OpenCV rectangle method
        cv2.rectangle(image, (left, top), (right, bottom), (255, 255, 1), 3)

    cv2.imshow("video", image)
    if cv2.waitKey(33) != -1:  
        pass
# Release capq
cap.release()

# Distroy windows
cv2.destroyAllWindows()