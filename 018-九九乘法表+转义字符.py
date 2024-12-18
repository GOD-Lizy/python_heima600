row=1
col=1
while(row<=9):
    while(col<=row):
        print("%d*%d=%d\t"%(col,row,row*col),end=" ")#哪一列没有对齐加个\t即可在垂直方向上对齐   这叫做转义字符中的制表符
        col+=1
    print("")
    col=1#这一个可以放在第二个while前面
    row+=1