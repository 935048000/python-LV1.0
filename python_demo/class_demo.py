"""内置方法 说明:
 __init__(self,...) 初始化对象，在创建新对象时调用
 __del__(self) 释放对象，在对象被删除之前调用
 __new__(cls,*args,**kwd) 实例的生成操作
 __str__(self) 在使用print语句时被调用
 __getitem__(self,key) 获取序列的索引key对应的值，等价于seq[key]
 __len__(self) 在调用内联函数len()时被调用
 __cmp__(stc,dst) 比较两个对象src和dst
 __getattr__(s,name) 获取属性的值
 __setattr__(s,name,value) 设置属性的值
 __delattr__(s,name) 删除name属性
 __getattribute__() __getattribute__()功能与__getattr__()类似
 __gt__(self,other) 判断self对象是否大于other对象
 __lt__(slef,other) 判断self对象是否小于other对象
 __ge__(slef,other) 判断self对象是否大于或者等于other对象
 __le__(slef,other) 判断self对象是否小于或者等于other对象
 __eq__(slef,other) 判断self对象是否等于other对象
 __call__(self,*args) 把实例对象作为函数调用
"""


""" 
__init__ ():
__init__方法在类的一个对象被建立时，马上运行。
这个方法可以用来对你的对象做一些你希望的初始化。
注意，这个名称的开始和结尾都是双下划线。

说明：__init__方法定义为取一个参数name（以及普通的参数self）。
在这个__init__里，我们只是创建一个新的域，也称为name。
注意它们是两个不同的变量，尽管它们有相同的名字。点号使我们能够区分它们。
最重要的是，我们没有专门调用__init__方法，只是在创建一个类的新实例的时候，
把参数包括在圆括号内跟在类名后面，从而传递给__init__方法。这是这种方法的重要之处。
现在，我们能够在我们的方法中使用self.name域。
这在sayHi方法中得到了验证。

代码例子:"""
class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hello, my name is', self.name)

p = Person ('Swaroop')
p.sayHi ()
# Hello, my
# name is Swaroop



"""
__new__ ():
__new__ ()在__init__ ()之前被调用，用于生成实例对象.
利用这个方法和类属性的特性可以实现设计模式中的单例模式.单例模式是指创建唯一对象吗，
单例模式设计的类只能实例化一个对象.
"""
class Singleton (object):
    __instance = None  # 定义实例

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):  # 在__init__之前调用
        if Singleton.__instance is None:  # 生成唯一实例
            Singleton.__instance = object.__new__ (cls, *args, **kwd)
        return Singleton.__instance


"""
__getattr__ ()、__setattr__ ()

和__getattribute__ ():
当读取对象的某个属性时，python会自动调用__getattr__ ()
方法.例如，fruit.color将转换为fruit.__getattr__ (color).当使用赋值语句对属性进行设置时，python会自动调用__setattr__ ()
方法.__getattribute__ ()的功能与__getattr__ ()类似，用于获取属性的值.
但是__getattribute__ ()能提供更好的控制，代码更健壮.
注意，python中并不存在__setattribute__ ()方法.
代码例子：
"""
class Fruit (object):
    def __init__(self, color="red", price=0):
        self.__color = color
        self.__price = price

    def __getattribute__(self, name):  # 获取属性的方法
        return object.__getattribute__ (self, name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value


if __name__ == "__main__":
    fruit = Fruit ("blue", 10)
    print()
    fruit.__dict__.get ("_Fruit__color")  # 获取color属性
    fruit.__dict__["_Fruit__price"] = 5
    print()
    fruit.__dict__.get ("_Fruit__price")  # 获取price属性

"""
__getitem__ ():

如果类把某个属性定义为序列，可以使用__getitem__ ()
输出序列属性中的某个元素.假设水果店中销售多钟水果，可以通过__getitem__ ()
方法获取水果店中的没种水果

代码例子:
"""
def __getitem__(self, i):  # 获取水果店的水果
    return self.fruits[i]


if __name__ == "__main__":
    shop = FruitShop ()
    shop.fruits = ["apple", "banana"]
    print(shop[1])
    for item in shop:  # 输出水果店的水果
        print(item,)
# banana
#
# apple
# banana

"""
__str__ ():
__str__ ()用于表示对象代表的含义，返回一个字符串.实现了__str__ ()
方法后，可以直接使用print语句输出对象，也可以通过函数str ()
触发__str__ ()的执行.这样就把对象和字符串关联起来，便于某些程序的实现，可以用这个字符串来表示某个类

代码例子：
"""
class Fruit:
    '''Fruit类'''  # 为Fruit类定义了文档字符串

    def __str__(self):  # 定义对象的字符串表示
        return self.__doc__


if __name__ == "__main__":
    fruit = Fruit ()
    print(str (fruit))
      # 调用内置函数str()出发__str__()方法，输出结果为:Fruit类
    print( fruit)
     # 直接输出对象fruit,返回__str__()方法的值，输出结果为:Fruit类

"""
__call__ ():
在类中实现__call__ ()
方法，可以在对象创建时直接返回__call__ ()
的内容.使用该方法可以模拟静态方法

代码例子:
"""
class Fruit:
    class Growth:  # 内部类
        def __call__(self):
            print("grow ...")

    grow = Growth ()  # 调用Growth()，此时将类Growth作为函数返回,即为外部类Fruit定义方法grow(),grow()将执行__call__()内的代码


if __name__ == '__main__':
    fruit = Fruit ()
    fruit.grow ()  # 输出结果：grow ...
    Fruit.grow ()  # 输出结果：grow ...