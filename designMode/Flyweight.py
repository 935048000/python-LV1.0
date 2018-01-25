"""

享元模式
"""

# 假设有一个网上咖啡选购平台，客户可以在该平台上下订单订购咖啡，平台会根据用户位置进行线下配送。
class Coffee:
    name = ''
    price =0
    def __init__(self,name):
        self.name = name
        self.price = len(name)
        # 在实际业务中，咖啡价格应该是由配置表进行配置，
        # 或者调用接口获取等方式得到，此处为说明享元模式，
        # 将咖啡价格定为名称长度，只是一种简化
        
    def show(self):
        print ("咖啡的名字:%s 价格:%s" % (self.name, self.price))


# 顾客类
class Customer:
    name=""
    def __init__(self,name):
        self.name=name
    def order(self,coffee_name):
        print ("%s 点了一杯咖啡:%s" % (self.name, coffee_name))
        return Coffee(coffee_name)


# 在咖啡实例化前，增加一个控制实例化的类：咖啡工厂。
# getCoffeeCount直接返回当前实例个数
class CoffeeFactory():
    coffee_dict = {}
    def getCoffee(self, name):
        if name not in self.coffee_dict:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]
    def getCoffeeCount(self):
        return len(self.coffee_dict)


# Customer类重写
class Customer2:
    coffee_factory=""
    name=""
    def __init__(self,name,coffee_factory):
        self.name=name
        self.coffee_factory=coffee_factory
    def order(self,coffee_name):
        print ("%s 点了一杯咖啡:%s" % (self.name, coffee_name))
        return self.coffee_factory.getCoffee(coffee_name)


# 短时间内有多人订了咖啡，业务模拟如下
if __name__=="__main__":
    coffee_factory=CoffeeFactory()
    customer_1=Customer2("A 客户",coffee_factory)
    customer_2=Customer2("B 客户",coffee_factory)
    customer_3=Customer2("C 客户",coffee_factory)
    c1_capp=customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha=customer_2.order("mocha")
    c2_mocha.show()
    c3_capp=customer_3.order("mocha")
    c3_capp.show()
    print ("咖啡的实例个数:%s" % coffee_factory.getCoffeeCount ())








