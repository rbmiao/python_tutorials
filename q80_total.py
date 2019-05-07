
#!/usr/bin/python
# -*- coding: UTF-8 -*-
def peach(monkey=5):     
    pea = 4  ##最后一个猴子分完剩余的桃子
    while 1:         
        tot_num = pea         
        for i in range(monkey):             
            tot_num = tot_num + tot_num / 4 + 1
            if tot_num % 1 != 0:  ##如果分出了小数则结束内层循环
                pea += 4  ##最后的桃子一定是4的整数倍
                break
        if tot_num % 1 == 0:  ##如果是整分 则结束
            break
        #print(pea, tot_num)
    return pea, tot_num 

if __name__ == '__main__':     
    pea, tot_num = peach()     
    print(pea, tot_num)
