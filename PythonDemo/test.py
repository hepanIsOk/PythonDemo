#
#输入：a = "0123456789"
#输出：02468 
#
L = [0, 1, 8, 3, 4]
L.sort()
print(L)
if len(L)%2==0:#偶
	print((L[int(len(L)/2)]+L[int(len(L)/2)-1])/2)
else:
	print(L[int(len(L)/2)])
