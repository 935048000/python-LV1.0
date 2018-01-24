"""

装饰器模式
"""

# 饮料类：
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


# 定义装饰器类
"""
卖可乐时，可以选择加冰，如果加冰的话，要在原价上加0.3元；
卖牛奶时，可以选择加糖，如果加糖的话，要原价上加0.5元。
"""
class drinkDecorator ():
    def getName(self):
        pass
    
    def getPrice(self):
        pass


class iceDecorator (drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getName(self):
        return self.beverage.getName () + " +ice"
    
    def getPrice(self):
        return self.beverage.getPrice () + 0.3


class sugarDecorator (drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getName(self):
        return self.beverage.getName () + " +sugar"
    
    def getPrice(self):
        return self.beverage.getPrice () + 0.5



if  __name__=="__main__":
    coke_cola=coke()
    print ("Name:%s" % coke_cola.getName ())
    print ("Price:%s" % coke_cola.getPrice ())
    ice_coke=iceDecorator(coke_cola)
    print ("Name:%s" % ice_coke.getName ())
    print ("Price:%s" % ice_coke.getPrice ())











