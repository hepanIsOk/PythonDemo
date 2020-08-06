#最小公约数
#a*b = [a,b]*(a,b)
a = input("a=")
b = input("b=")
try:
	d = int(a)*int(b)
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
except :
	print("输入格式出错，必须是正整数")
else :
	print("最小公倍数：",d/b)