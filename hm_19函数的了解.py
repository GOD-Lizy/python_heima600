#  需求：修改文件，增加的数定义&multiple_table():
# 新建另外一个文件，使用import导入并且调用图数
def mutiple_table (): #定义函数操作
    row=1
    col=1
    while(row<=9):
        while(col<=row):
            print("%d*%d=%d\t"%(col,row,row*col),end=" ")#哪一列没有对齐加个\t即可在垂直方向上对齐   这叫做转义字符中的制表符
            col+=1
        print("")
        col=1#这一个可以放在第二个while前面
        row+=1
row = 1
col = 1
while(row<=9):
    col = 1
    while(col<=row):
        print("%d*%d=%d\t"%(col,row,col*row),end=" ")
        col+=1
    print("")
    row+=1









