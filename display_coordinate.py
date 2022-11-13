
face_tuple = [(67,382,196,253)]
print(face_tuple)
for face in face_tuple:
	# for value in value:
	# print(value)
	pass


for (top,right,bottom,left) in face_tuple:
	x1=left
	y1=top
	x2=right
	y2=bottom
	print((x1,y1),(x2,y2))

