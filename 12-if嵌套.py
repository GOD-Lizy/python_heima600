"""
定义布尔型变量,has_ticket,判断是否有车票
定义整型变量knife_leghth，表示刀的长度，单位是厘米
首先检查是否有车票，有的话允许进行安检
安检时需要检查刀的长度，判断是否超过20厘米
如果超过20厘米，提示刀的长度，不允许上车
如果不超过20厘米，允许上车
如果没有车票不允许进门
"""
has_ticket = bool(int(input("请输入有无车票")))
knife_leghth = float(input("请输入刀子的长度"))
if(has_ticket == True):
    if(knife_leghth >= 20 ):
        print("不允许上车，你携带的刀子的长度为%0.3f厘米"%knife_leghth)
    else:
        print("允许上车")
else:
    print("不允许进门")