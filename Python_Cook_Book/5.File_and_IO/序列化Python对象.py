#!/usr/bin/env python
# coding=utf-8


'''
需要将一个 Python 对象序列化为一个字节流
以便将它保存到一个文件、存储到数据库或者通过网络传输它。
序列化最普遍的做法就是使用 pickle 模块

pickle 在加载时有一个副作用就是它会自动加载相应模块并构造实例对象。
但是坏人他就可以创建一个恶意的数据导致 Python 执行随意指定的系统命令。
因此，一定要保证 pickle 只在相互之间可以认证对方的解析器的内部使用。

'''


import pickle
data = 'Some Python object'
f = open('somefile', 'wb')
pickle.dump(data, f)
s = pickle.dumps(data)
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)

f.close()

#从文件中恢复
f = open('somefile', 'rb')
dataf = pickle.load(f)
print dataf
dataf = pickle.load(f)
print dataf
dataf = pickle.load(f)
print dataf

#从string中恢复
datas = pickle.loads(s)
print datas

import math
print pickle.dumps(math.cos)
print

import time
import countdown
c = countdown.Countdown(30)

time.sleep(6)
print
f = open('cstate.p', 'wb')
pickle.dump(c, f)
f.close()
print
f = open('cstate.p', 'rb')
pickle.load(f)
time.sleep(6)









