# 需求：在控制台连续输出五行*来，每一行是号的量次递增
# 第一种做法：
a = "*"
i = 1
while(i<=5):
    print(a)
    i += 1
    a += "*"
# 第二种做法：
a = 1
while(a<=5):
    print("*"*a)
    a+=1
# 第三种做法：
# print("*",end="")#小扩展：后面加end=""，可以消除print的自动换行操作
# print("*")
row=0
col=0
while(row<=4):
    while(col<=row):
        print("*",end="")
        col+=1
    col=0
    print("")#换行操作
    row+=1
