
# 需求
# 1.从控制台输入要出的拳--石头(1)/剪刀(2)/布(3)2.电脑 随机 出拳--先假定电脑只会出石头，完成整体代码功能
# 3.比较胜负
import random
player = int(input("请输入您要出的东西 拳头/1 剪刀/2 布/3"))
computer = random.randint(1,3)
print("您的数字为%d,而电脑的数字为%d"%(player,computer))
if ((player == 1 and computer==2)
        or (player == 2 and computer==3)
        or (player == 3 and computer==1)):
    print("玩家胜利")
elif(player == computer):
    print("平局")
else:
    print("电脑胜利")