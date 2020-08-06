# 回文字符串
# s = "abcba"
# n= 5
# L = list(s)

# for i in range(len(L)-n+1):
# 	a = L[i:i+n]
# 	print(a)
# 	b =list(reversed(a))
# 	print(b)
# 	if a ==b:
# 		print("YES")
# 		break
#find()获取字符串未知
# a = "OurWorldIsFullOfLOVwE"

# b = a.upper().find('LOVE')
# if b == -1:
# 	print("single")
# else:
# 	print("love")




#内置函数 chr()将ASC序号转换成对应的字符串；ord()将ASC字符串转换成序号
# a = "cagy" 
# b = 3
# s = ""
# L = list(a)
# for i in L:
# 	if ord(i)-96+b > 26:
# 		s+=chr(ord(i)+b-26)
# 		#print(chr(ord(i)+b-26))
# 	else :
# 		s+=chr(ord(i)+b)
# 		print(chr(ord(i)+b))
# 	# print(chr(ord(i)+3))

# print(s)
