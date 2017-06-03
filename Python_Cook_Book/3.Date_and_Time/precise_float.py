#!/usr/bin/env python
# coding=utf-8


'''
执行精确的浮点数运算
对浮点数执行精确的计算操作，并且不希望有任何小误差的出现
浮点数的一个普遍问题是它们并不能精确的表示十进制数
即使是最简单的数学运算也会产生小的误差
decimal 模块实现了 IBM 的” 通用小数运算规范”。
'''


a=5.2
b=4.1
c=a+b
print c
print a+b

print c==9.3
print

#更加精确 (并能容忍一定的性能损耗)，你可以使用 decimal 模块
from decimal import Decimal
a=Decimal('5.2')
b=Decimal('3.2')
c=a+b
print a+b
print c
print c==8.4
print


from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)


with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)









