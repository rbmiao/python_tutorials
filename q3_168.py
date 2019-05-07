#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#
# 程序分析：
#
# 假设该数为 x。
#
# 1、则：x + 100 = n2, x + 100 + 168 = m2
#
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
#
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
#
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
#
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
#
# 7、接下来将 i 的所有数字循环计算即可。
 
# for i in range(1,85):
#    if 168 % i == 0:
#        j = 168 / i;
#        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#            m = (i + j) / 2
#            n = (i - j) / 2
#
#            x = n * n - 100
#            print("i={}\tj={}\tm={}\tn={}\tx={}".format(i, j, m, n, x))



#for m in range(168):
#    for n in range(m):
#        if (m+n)*(m-n)==168:
#            x=n**2-100
#            print("符合条件的整数有:{}".format(x))


'''
分析：
设这个整数为x
1、 x+100=n^2和x+100+168=m^2
推出 m^2-n^2=168
即   （m+n)(m-n)=168
设    m+n=i m-n=j
则    i*j=168
由    i>0 j>0   推出  i%2=0 j%2=0
由    168=2*2*2*3*7
上面两个条件推出i与j值的范围[2,4,6,12,14,28,42,84]
反推：m=(i+j)/2和n=(i-j)/2 并且 n>0 推得 i>j
则     i=[14,28,42,84]
       j=[12,6,4,2]
'''
# arr1=[14,28,42,84]
# arr2=[12,6,4,2]
# for i in range(0,4):
#     m=(arr1[i]+arr2[i])/2
#     n=(arr1[i]-arr2[i])/2
#     x=n*n-100
#     print(x)

class Num:
    def __init__(self):
        pass
    def calc(self):
        for i in range(2,86):
            for j in range(2,86):
                if (i * j == 168) and (i > j):
                    # print(i,j)
                    if ((i % 2 == 0) and (j % 2 ==0)) or ((i % 2 != 0) and (j % 2 !=0)):
                        n = (i-j)/2
                        d = int(n*n -100)
                        print(d)
a = Num().calc()