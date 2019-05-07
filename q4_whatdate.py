#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# 
##
import os 


year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))


p = [31,28,31,30,31,30,31,31,30,31,30,31]


print(('year={}, month={},  day={}').format(year, month, day))

if year % 100 == 0 and year % 400 != 0:
    print('leap year')
    days = sum(p[0:month-1]) + day
else:
    print('Not leap year')
    days = sum(p[0:month-1]) + day + 1

days = sum(p[0:month-1]) + day

print('it is {}th day'.format(days))