L = [0, 1, 2, 3, 4,4]

L1 = list(sorted(L))
L2 =  list(sorted(L,reverse=True))

print(L)
print(L1)
if L == L1:
	print("UP")
elif L==L2:
	print("DOWN")
else:
	print("WRONG")

for i in range(len(L1)-1):
	if L1[i] == L1[i+1]:
		print("YES")
		break
