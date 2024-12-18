# 需求：定义一个字符串变量name，输出我的名字是小明，请多多关照！
"""
name = "小明"
print("我的名字是%s"%name)
"""
# 需求：定义整数变量student_num，并输出000001
"""
student_num = 1
print("你的学号是%06d"%student_num)#%0nd输出显示n位的整数，不足的地方用0补齐
"""
# 定义一个小数scale，输出数据比例是10.00%
scale = 0.2
print("%0.3f%%" %(scale*100))


a=input("请输入苹果的重量")
weight=float(a)
b=input("请输入苹果的单价")
soar=float(b)
print("顾客你需要支付的金额是%.03f，你买了%.03f斤，单价为%.03f元" %(weight*soar,weight,soar))#%.0nf显示小数点后n位