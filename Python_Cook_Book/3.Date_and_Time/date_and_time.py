#!/usr/bin/env python
# coding=utf-8


'''
基本的日期与时间转换

执行简单的时间转换，比如天到秒，小时到分钟等的转换

执行不同时间单位的转换和计算，请使用 datetime 模块

需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等，可以考虑使用 dateutil 模块
dateutil在处理月份 (还有它们的天数差距) 的时候填充间隙。
'''

from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c=a+b

print c.days
print c.seconds
print c.seconds /3600
print c.total_seconds() /3600
print

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d=b-a
print d.days
now=datetime.today()
print now
print now + timedelta(minutes=10)
print

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print a - b
print (a - b).days

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print (c - d).days
print

# 字符串转换为日期
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print diff



