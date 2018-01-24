
"""
建造者模式
"""

# 主餐
class Burger():
    name=""
    price=0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="芝士汉堡"
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="香辣鸡腿汉堡包"
        self.price=15.0

# 小食
class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "鸡翅膀"
        self.price = 12.0


# 饮料
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "可乐"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "牛奶"
        self.price = 5.0


# 订单类

class order():
    burger=""
    snack=""
    beverage=""
    def __init__(self,orderBuilder):
        self.burger=orderBuilder.bBurger
        self.snack=orderBuilder.bSnack
        self.beverage=orderBuilder.bBeverage
    def show(self):
        print ("汉堡包:%s" % self.burger.getName ())
        print ("小吃:%s" % self.snack.getName ())
        print ("饮料:%s" % self.beverage.getName ())


# orderBuilder就是建造者模式中所谓的“建造者”
class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""
    def addBurger(self,xBurger):
        self.bBurger=xBurger
    def addSnack(self,xSnack):
        self.bSnack=xSnack
    def addBeverage(self,xBeverage):
        self.bBeverage=xBeverage
    def build(self):
        return order(self)

# Director类，用以安排已有模块的构造步骤。
# 对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。
class orderDirector():
    order_builder=""
    def __init__(self,order_builder):
        self.order_builder=order_builder
    def createOrder(self,burger,snack,beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


if  __name__=="__main__":
    order_builder=orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    order_1=order_builder.build()
    order_1.show()