def cycle(numerator,denominator):
    cycle_length = 0#循环节长度
    dec = list()#存放小数
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
    text = str(dec[0]) + "."
    while i < len(dec): 
        if i == p + 1:
            text+="["
        text+=str(dec[i])
        i+=1
    if p >= 0:
        text+="]"+'\n'
    print(text)
    print("循环节个数:"+str(cycle_length))


numerator=10 #被除数 
denominator=13#除数
print(numerator/denominator)
cycle(numerator, denominator)



