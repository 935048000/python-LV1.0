#/usr/bin/env python

import MySQLdb

conn = MySQLdb.Connect(host='localhost', user='root', passwd='root', db='python', charset='utf8')

#多条语句插入：
value = [1, 'hello']
cur.execute('insert into test values(%s,%s)', value)
#或
values = []
for i in range(20):
    values.append((i, 'hi rollen' + str(i)))

#常用的函数：

#然后, 这个连接对象也提供了对事务操作的支持, 标准的方法
commit()
#提交

rollback()
#回滚

#cursor用来执行命令的方法:
callproc(self, procname, args)
#用来执行存储过程, 接收的参数为存储过程名和参数列表, 返回值为受影响的行数

execute(self, query, args)
#执行单条sql语句, 接收的参数为sql语句本身和使用的参数列表, 返回值为受影响的行数

executemany(self, query, args)
#执行单挑sql语句, 但是重复执行参数列表里的参数, 返回值为受影响的行数

nextset(self)
#移动到下一个结果集

#cursor用来接收返回值的方法:
fetchall(self)
#接收全部的返回结果行.

fetchmany(self, size=None)
#接收size条返回结果行.如果size的值大于返回的结果行的数量, 则会返回cursor.arraysize条数据.

fetchone(self)
#返回一条结果行.

scroll(self, value, mode='relative')
#移动指针到某一行.如果mode = 'relative', 则表示从当前所在行移动value条
# #如果mode = 'absolute', 则表示从结果集的第一行移动value条.
