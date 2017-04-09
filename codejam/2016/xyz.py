def func1(x):
	list2.append(1)
	list2.append(2)
	list2.append(3)
	if x==1:	
		list1.append(list2)
		list1.append(list2)
	return 0

for i in range(2):
	list1 = []
	list2 = []
	func1(1)
	print list1