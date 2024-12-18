#python中定义变量不需要定义类型，它会根据等号右边的数据自动推导出保存数据的类型
name = "小明"

age = 69

gender = True#小明是男生

name = "xiaoming"
print(type(name))
print(type(age))
print(type(gender))
print(type(2 ** 32))
print(type(2 ** 64))#在python3中输出为int 而在python2中输出为long
print(10+True)#布尔型数字参与运算时True为1，False为0
print(10+False)
Firstname = "三"
Lastname = "张"
name = Lastname + " " + Firstname
name2 = (name+" ")*10#字符串类型也可以参与运算，但注意不能字符串与整数相加
#print(name+1)这是错误的示范 会报错无法将整型转化为字符串
print(name)
print(name2)
