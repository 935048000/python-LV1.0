"""

模板模式

据股票代码来查询股价分为如下几个步骤：登录、设置股票代码、查询、展示。
"""

# 虚拟股票查询器
class StockQueryDevice():
    stock_code = "0"
    stock_price = 0.0
    
    def login(self, usr, pwd):
        pass
    
    def setCode(self, code):
        self.stock_code = code
    
    def queryPrice(self):
        pass
    
    def showPrice(self):
        pass
    
    def operateQuery(self, usr, pwd, code):
        if not self.login (usr, pwd):
            return False
        self.setCode (code)
        self.queryPrice ()
        self.showPrice ()
        return True


# WebA和WebB的查询器类
class WebAStockQueryDevice(StockQueryDevice):
    def login(self,usr,pwd):
        if usr=="myStockA" and pwd=="myPwdA":
            print ("Web A:Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print ("Web A:Login ERROR... user:%s pwd:%s" % (usr, pwd))
            return False
    def queryPrice(self):
        print ("Web A Querying...code:%s " % self.stock_code)
        self.stock_price=20.00
    def showPrice(self):
        print ("Web A Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))


class WebBStockQueryDevice(StockQueryDevice):
    def login(self,usr,pwd):
        if usr=="myStockB" and pwd=="myPwdB":
            print ("Web B:Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print ("Web B:Login ERROR... user:%s pwd:%s" % (usr, pwd))
            return False
    def queryPrice(self):
        print ("Web B Querying...code:%s " % self.stock_code)
        self.stock_price=30.00
    def showPrice(self):
        print ("Web B Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))


if  __name__=="__main__":
    # web_a_query_dev=WebAStockQueryDevice()
    # web_a_query_dev.login("myStockA","myPwdA")
    # web_a_query_dev.setCode("12345")
    # web_a_query_dev.queryPrice()
    # web_a_query_dev.showPrice()

    web_a_query_dev = WebAStockQueryDevice ()
    web_a_query_dev.operateQuery ("myStockA", "myPwdA", "12345")




















