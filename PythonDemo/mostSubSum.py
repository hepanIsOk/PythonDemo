#求L的一个连续子序列，使其和最大

# L=[2,3,-3,50,-6]
# result = []
# for  i in range(len(L)-1):
#     maxx = L[i]
#     LL = []
#     for x in range(i+1,len(L)):
#         maxx += L[x]
#         LL.append(maxx)
#     num = max(LL)
#     result.append(num)
# print(max(result))

n = 2992

# b = bin(n)
h = list(hex(n))
print(h[2:])
text1 = 0
for i in h[2:]:
	if i == 'a':
		text1+=10
	elif i == 'b':
		text1+=11
	elif i == 'c':
		text1+=12
print(text1)
i=0
a = list()
while n!=0:
	a.insert(i,n%12)
	n//=12
	i+=1

print(a)
