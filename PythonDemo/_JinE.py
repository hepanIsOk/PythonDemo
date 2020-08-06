#在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万
def getNum(param):
	# print("返回数字大写")
	if param == '0':
		return "零"
	elif param == '1':
		return "壹"
	elif param == '2':	
		return "贰"
	elif param == '3':	
		return "叁"
	elif param == '4':	
		return "肆"
	elif param == '5':	
		return "伍"
	elif param == '6':	
		return "陆"
	elif param == '7':	
		return "柒"
	elif param == '8':	
		return "捌"	
	elif param == '9':	
		return "玖"			
	else:
		return "未知"

def getUnit(fa,flag):
# 返回单位
	text ="万"
	ss =[]
	if flag == 1:#0-前四位；1-后四位
		text ="圆"
		if len(fa) == 1:#0
			return getNum(fa[0])+"圆"
	
	for i in range(len(fa)):
		if i == 0:
			if fa[i] == '0' and flag == 1:
				ss.insert(0,"圆")
			elif fa[i] == '0' and flag == 0:
				ss.insert(0,"零")
			else:
				ss.insert(0,getNum(fa[i]) +text)
		elif i == 1:
			if fa[i] == '0' and fa[i-1] != '0':
				ss.insert(0,"零")
			elif fa[i] == '0' and fa[i-1] == '0':
				continue
			else:
				ss.insert(0,getNum(fa[i])+"拾" )
		elif i == 2:
			if fa[i] == '0' and fa[i-1] != '0':
				ss.insert(0,"零")
			elif fa[i] == '0' and fa[i-1] == '0':
				continue
			else:
				ss.insert(0,getNum(fa[i])+"佰" )
		elif i == 3:
			if fa[i] == '0' and fa[i-1] != '0':
				ss.insert(0,"零")
			elif fa[i] == '0' and fa[i-1] == '0':
				continue
			else:
				ss.insert(0,getNum(fa[i])+"仟" )
	return ss

def getAmount(a):
	#获取整个金额
	ret = ""
	if a <0:
		ret = "负"
	L = list(str(abs(a)))
	fa =[]
	fb =[]
	if len(L) <= 8 and len(L) >4:
		fa.extend(L[:len(L)-4])#前段
		fb.extend(L[len(L)-4:])#后段
	elif len(L) <= 4 and len(L) >0:
		fb.extend(L)#后段
	else:
		return "请输入小于100000000的整数"
	# print(fa,fb)
	fa.reverse()
	fb.reverse()
	ss = getUnit(fa,0)
	bb = getUnit(fb,1)	
	return ret+"".join(ss)+"".join(bb)

i = 0
while i<10:
	i = i+1
	a= input("input:")
	try:
		b=int(a)
		print(getAmount(b))
	except :
		print("请输入小于100000000的整数")

	



# a= 7
# count = 0
# print(list(bin(a)).count('1'))
# for i in list(bin(a)):
# 	if i == '1':
# 		count +=1
# print(count)		

# a = "KDJIskos234k,.;djfeiJ"
# print(a.lower())


