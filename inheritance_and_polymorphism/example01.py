

class people(object):
    def run(self):
        print("the is people\n")


people.run(object)
# the is people

# 继承父类people
# class eye(people):
#     pass
#
# class nose(people):
#     pass
#
# EYE = eye()
# EYE.run()
# # the is people
#
# NOSE = nose()
# NOSE.run()
# # the is people

# 父类 和 子类的方法冲突
class eye(people):
    def run(self):
        print("the is eye\n")

class nose(people):
    def run(self):
        print("the is nose\n")

EYE = eye()
EYE.run()
# the is eye

NOSE = nose()
NOSE.run()
# the is nose

# 类就是一种数据类型,子类继承父类的数据类型，子类的实例有两种数据类型
# print(isinstance(EYE,eye))
# print(isinstance(EYE,people))
# # True
# # True


# 多态的好处
def run_two(people):
    people.run()
    people.run ()

run_two(people())
# the is people
# the is people

run_two(eye())
# the is eye
# the is eye

run_two(nose())
# the is nose
# the is nose


# 新增一个的子类，不必对原方法做任何修改
# 任何依赖父类作为参数的函数或者方法都可以不加修改地正常运行
class hand(people):
    def run(self):
        print("the is hand\n")

run_two (hand ())
# the is hand
# the is hand

# 传入的任意类型，只要是父类类或者子类，就会自动调用实际类型的方法，
# 继承还可以一级一级地继承下来，继承关系看上去就像一颗倒着的树。

# 继承的 好处：1.子类获得父类所有功能；2.多态
# 多态：依赖于继承。子类的实例的数据类型既可以是子类，也可以是子类的父类。
# 多态的好处：依赖于父类的函数需要传入子类时，只需要接受父类即可。
