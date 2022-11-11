import cv2

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()
	frame = cv2.cvtColor(src=frame,code=cv2.COLOR_BGR2RGB)
	cv2.imshow('webcam',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()