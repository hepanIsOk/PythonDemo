for i in range(101):
	if i%7==0:
		continue
	elif str(i).find('7') != -1:
		continue
	else:
		print(i)