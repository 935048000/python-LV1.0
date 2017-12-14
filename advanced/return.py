#coding=utf-8
# 闭包:返回函数


# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 每次调用lastsum()都会返回一个新的函数，即使传入相同的参数

def lastsum(*args):
    def sum():
        x = 0
        for i in args:
            #x = x + i
            x += i
        return x
    return sum

s = lastsum(1,2,3,4,5)
print s
print s()


# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 返回的函数并没有立刻执行，而是直到调用了f()才执行。
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print f1()
# print f2()
# print f3()
print
def count():
    def f(j):
        # def g():
        #     return j*j
        #return g
        return j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
# 闭包，返回函数
# print f1()
# print f2()
# print f3()
# 非闭包，返回值
print f1
print f2
print f3













