# break和continue是只在循环内部使用的关键字
# break某一条件满足时，退出循环，不再执行后续重复的代邵某一条件满足时，不执行后续近复的代码continuebreak和continue只针对当前所在环有效
# break continue 都是用在循环体内的
i = 0
while(i <= 10):
     print(i)
     if(i == 3):
         break
     i += 1
a = 0
while a < 10:# 这段程序能输出除了3之外0到10的所有数字
    if(a == 3 ):
        a += 1
        continue
    print(a)
    a+=1
