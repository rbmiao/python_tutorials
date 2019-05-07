#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
#
 
if __name__ == '__main__':
    # 方法一 ： 0 作为加入数字的占位符
    a = [2,4,6,9,13,16,19,28,40,100,0]
    print(len(a))
    print(a)
    #print('原始列表:')
    #for i in range(len(a)):
    #    print(i, a[i])

    insertn=int(input("Please input a number: \n"))
    'This is for commenting'
    print(insertn)

    if insertn >= a[len(a)-2]:
        a[len(a) - 1 ] = insertn
        #break
    elif a[0] > insertn:
        for j in range(len(a)-1):
                #print(i, j, a[i], a[j])
            a[len(a)-j-1] = a[len(a)-j-2]
        a[0] = insertn
    else:
        for i in range(len(a)-1):
            # a[i] < insertn:
            print('daniel {} ai={} in={} ai1={}'.format(i, a[i], insertn, a[i+1]))

            if a[i+1] >= insertn > a[i]:
                #print('Here we go:')
                #print(i, a[i], insertn, a[i+1])
                for j in range(len(a)-1, i, -1):
                    #print(j, a[j-1], a[j])
                    a[j] = a[j-1]
                a[i+1]    = insertn
                break
            else: 
            	continue
            
            break

            #a[i] = insertn
    print("New ", "array is {}". format(a))    