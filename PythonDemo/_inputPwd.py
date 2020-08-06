# 输出密码 
# 正整数a和b:a,b,x,y（0 < a,b <= 20132013, 0 < x <= y < 100000000000)

def cycle(numerator,denominator,dec):
    cycle_length = 0#循环节长度
    rem = list()#存放余数
    p = -1#循环节的起始位置 -1
    while True:
        dec.append(numerator // denominator)#存储一位小数 0 1 4 2 8 5 7 1
        x = numerator % denominator #x作为余数
        if x == 0:#余数为零,退出循环
            cycle_length = 0
            break        
        try:
            p = rem.index(x)#判断余数是否存在
        except :
            p = -1
        if p > -1:
            break
        rem.append(x)#存储一位余数 1 3 2 6 4 5 1
        cycle_length+=1
        numerator = x * 10#在余数后面添零,作为下一个被除数

    i = 1
    text = ""
    while i < len(dec): 
        text+=str(dec[i])
        i+=1
    return cycle_length

def printF(a,b,x,y):	
	temp = list()
	print("小数："+str(a/b))
	text = cycle(a,b,temp)

	L = list(map(str,temp[1:]))
	# print("循环节："+''.join(L))
	num = len(L)
	ret = ""
	if text == 0:
		if num ==0:
			ret = '0'*(y-x+1)
		else:
			if y-x >= num:
				n = (y-x+1 - (num -x%num) - y%num)
				ret = ''.join(L[x%num-1:])+'0'*n+''.join(L[:y%num])
			else:
				if y%num > y-x:
					ret = ''.join(L[x%num-1:y%num])
				else:
					ret = ''.join(L[x%num-1:])+''.join(L[:y%num])
	else:   #循环小数
		if y-x >= num:
			n = (y-x+1 - (num - 1-x%num) - y%num)//num
			ret = ''.join(L[x%num-1:])+''.join(L)*n+''.join(L[:y%num])
		else:
			if y%num > y-x:
				ret = ''.join(L[x%num-1:y%num])
			else:
				ret = ''.join(L[x%num-1:])+''.join(L[:y%num])
	print("密码："+ret)

a, b,x,y = map(int, input("请依次输入被除数 除数 密码起始位 密码结束位：").split()) 
printF(a,b,x,y)

