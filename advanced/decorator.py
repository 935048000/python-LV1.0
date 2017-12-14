#coding=utf-8


# 装饰器
# 一个返回函数的高阶函数
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
now()
print now.__name__

# 加入自定义日志功能，和__name__不改变
import functools

def lognew(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@lognew('execute')
def nownew():
    print('2015-3-25')
nownew()

print nownew.__name__

# 偏函数
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# 用于固定函数的某些参数
int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1000000', base=10)



