#!/usr/bin/env python
#coding=utf-8

import MySQLdb

#连接数据库
cnn=MySQLdb.connect(user='root',passwd='123',host='127.0.0.1')

#获取游标
cur=cnn.cursor()

#sql语句影响的行数
print 'sql语句影响的行数:',cur.execute('show databases')

#获取查询结果所有行
print '获取查询结果所有行:',cur.fetchall()


#关闭游标
cur.close()

#提交事务
#cnn.commit()

#断开sql连接
cnn.close()