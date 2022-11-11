import face_recognition
from PIL import Image, ImageDraw
import cv2

img = face_recognition.load_image_file("known_images/jobs_1.jpg")

face_loc = face_recognition.face_locations(img)
print(face_loc)

print("number of tuples",len(face_loc))

for face in face_loc :

	for value in face :
		print(value)

	print(face)

pil_image = Image.fromarray(img)
draw = ImageDraw.Draw(pil_image)
# 
#top right bottom left
#(67, 382, 196, 253)
#x1			y1
#(left=253, top = 67)
#x2		    y2
#(right=382,bottom =196)
draw.rectangle((253,67,382,196),outline="red",width=3)
pil_image.show()


# using open cv to display face image 
image_cv= cv2.imread('known_images/jobs_1.jpg')
cv2.cvtColor( src = image_cv, code = cv2.COLOR_BGR2RGB)
cv2.rectangle(image_cv, (253,67), (382,196), color=(255,0,0), thickness=2)
cv2.imshow('Display_Window',image_cv)

if cv2.waitKey(0) & 0xFF == ord('q'):
	pass
else:
	pass
cv2.destroyAllWindows()
