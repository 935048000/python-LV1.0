#coding=utf-8



# map()函数接收两个参数，一个是函数，一个是Iterable.
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = map(f,list1)
print (list2)


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上.
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def ADD(x,y):
    return x+y

list3 = reduce(ADD,list1)
print list3

def fn(x,y):
    return x * 10 + y
list4 = reduce(fn,list1)
print list4



def normalize(name):
    return name[0].upper()+name[1:].lower()

L = ['adam','LISA','barT','XXio']
L2 = list( map(normalize,L) )
print (L2)


# filter()接收一个函数和一个序列。
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()的作用是从一个序列中筛出符合条件的元素。
# 由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

# 删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print list(filter(is_odd, list1))

# 空字符串删掉
def not_empty(s):
    return s and s.strip()
print list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


# sorted()函数就可以对list进行排序
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
# 反向排序，不必改动key函数，可以传入第三个参数reverse=True
nlist = [36, 5, -12, 9, -21]
print  sorted(nlist)
print  sorted(nlist, key=abs)

print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

# 按名字和成绩排序
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def byname(L):
    return L[0]
def byscore(L):
    return L[1]
print  sorted(L, key=byname)
print  sorted(L, key=byscore,reverse=True)
