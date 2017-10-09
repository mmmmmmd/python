# -*- coding:utf-8 -*-
#含有多个返回值的函数
def calculate(data1,data2):
    sum = data1 + data2
    minus = data1 - data2
    multiply = data1 * data2
    divide = data1 / data2
    return sum,minus,multiply,divide

data1 = 5
data2 = 4
sum,minus,multiply,divide = calculate(data1,data2)
print "%d和%d的和为：%d" %(data1,data2,sum)
print "%d和%d的差为：%d" %(data1,data2,minus)
print "%d和%d的积为：%d" %(data1,data2,multiply)
print "%d和%d的分为：%d" %(data1,data2,divide)