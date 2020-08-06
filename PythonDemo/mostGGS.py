#求两数的最大公约数 
# c=a%b,c=0则b是最大公约数 ，否则a=b,b=c,继续计算a%b
a = input("a=")
b = input("b=")
c = 0
while 1:
	c = int(a)%int(b)
	#print("输出",c)
	if c == 0:
		print("最大公约数：",b)
		break
	else:
		a = b
		b = c
