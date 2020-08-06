# 给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。如果为奇数输出1,偶数则输出0.。
# 例如：L=[2,8,3,50]
# 则输出：0

L = [2, 8, 3, 50]
message = 1;
for item in L:
	if item % 2 ==0:
		message = 0
		break

print(message)
