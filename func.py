#!/usr/bin/python

def myfunc(arg1, *vartuple):
    'print any parameters'
    print("what are inputs:")
    print(arg1)
    print(vartuple)
    print("Rongbing")
    for vr in vartuple:
    	print(vr)
    return

myfunc(10)
myfunc(10, 30, 50, 60)

## 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
## 调用sum函数
print("相加后的值为 : {}".format(sum( 120, 200 )))
print("相加后的值为 : {}".format(sum( 230, 20 )))


#x = lambda a : a + 10

sum22 = lambda x, y : x + y
print(sum22(5, 6)) 