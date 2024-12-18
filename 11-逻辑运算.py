# 定义一个整数年龄age，要求年龄在0-120之间，设计代码判断是否正确(逻辑运算符and or not)
"""
age = int(input("请输入您的年龄"))
if(age>=0 and age<=120):
    print("你的年龄为%d"%age)
else:
    print("你的输入有问题")
"""
# 需求：定义两个整数变量python_score\c_score，编辑代码只要有一门成绩大于等于60就是合格
"""
python_score=int(input("请输入您的python成绩"))
c_score=int(input("请输入您的c成绩"))
if((python_score or c_score)>=60):
    print("你的成绩合格")
else:
    print("你的成绩不合格")
"""
# 需求：定义一个布尔型变量is_employee ,如果是本公司员工则可以入内，如果不是禁止入内
"""
is_employee = bool(int((input("请输入您的身份"))))
if(is_employee == True):
    print("您好，欢迎进入")
if not(is_employee == True):
    print("您没有权限进入")
"""
# 需求:输入今天的节日，如果是情人节就买鲜花，端午节就吃粽子，平安夜就吃苹果
today=input("请输入今天的节日")
if(today=="qingrenjie"):
    print("买鲜花")
elif(today=="duanwujie"):
    print("吃粽子")
elif(today=="pinganye"):
    print("吃苹果")
else:
    print("今天不过节日")