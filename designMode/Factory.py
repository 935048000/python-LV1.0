
"""
工厂模式
"""

# 汉堡
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
        

# 小食。
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
        self.name = "薯条"
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
        self.name = "可口可乐"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "牛奶"
        self.price = 5.0
        

# 工厂
class foodFactory():
    type=""
    def createFood(self,foodClass):
        print (self.type," 工厂产生一个实例.")
        foodIns=foodClass()
        return foodIns
class burgerFactory(foodFactory):
    def __init__(self):
        self.type="BURGER"
class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"


if  __name__=="__main__":
    burger_factory=burgerFactory()
    snack_factorry=snackFactory()
    beverage_factory=beverageFactory()
    cheese_burger=burger_factory.createFood(cheeseBurger)
    print (cheese_burger.getName(),cheese_burger.getPrice())
    chicken_wings=snack_factorry.createFood(chickenWings)
    print (chicken_wings.getName(),chicken_wings.getPrice())
    coke_drink=beverage_factory.createFood(coke)
    print (coke_drink.getName(),coke_drink.getPrice())