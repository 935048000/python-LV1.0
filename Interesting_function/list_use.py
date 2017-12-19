"""
列表操作
左右 增加/删除 元素
"""

# 一般写法
names = ["a","b","c"]
print(names)
names.pop(0) # delete
print(names)
names.insert(0,"d")
print(names)
names.append("e")
print(names)


# 高阶写法
from collections import deque

list = ["a","b","c"]
dequelist = deque(list)
print(dequelist)
dequelist.popleft()
print(dequelist)
dequelist.appendleft("d")
print(dequelist)
dequelist.append("e")
print(dequelist)


