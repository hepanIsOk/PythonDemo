#列表乘积末尾是0的个数 
# 思路：得到2的幂次和5的幂次，2*5 = 10 最小的次数就是0的
L = [4, 2, 25, 7777777, 100, 3, 77777777, 77777777, 77777777, 77777777]
t = 0
f = 0

for item in L:	
	while item%2 == 0:
		item = int(item)/2	
		t += 1 
		#print(item)
	while item%5 == 0:
		item = int(item)/5	
		f += 1 
		#print(item)
if t>f:
	print(f)
else:
	print(t)

