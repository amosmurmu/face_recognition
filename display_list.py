
list_tuples=[(78,56),(23,34),(33,45),(27,26),(30,12)]

first = 0 
next_value = 1
len_list = len(list_tuples)
value = 0
while(value < len_list-1):

	# print(first,next_value)
	print(list_tuples[first],list_tuples[next_value])
	value+=1
	first+=1
	next_value+=1
	