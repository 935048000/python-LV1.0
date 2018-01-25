"""

中介者模式

手机仓储管理系统，使用者有三方：销售、仓库管理员、采购。
需求是：销售一旦达成订单，销售人员会通过系统的销售子系统部分通知仓储子系统，
仓储子系统会将可出仓手机数量减少，同时通知采购管理子系统当前销售订单；
仓储子系统的库存到达阈值以下，会通知销售子系统和采购子系统，并督促采购子系统采购；
采购完成后，采购人员会把采购信息填入采购子系统，采购子系统会通知销售子系统采购完成，并通知仓库子系统增加库存。
引入一个新的角色-中介者-来将“网状结构”精简为“星形结构”。
"""

# 构造三个子系统,同事类
class colleague():
    mediator = None
    def __init__(self,mediator):
        self.mediator = mediator
        
        
class purchaseColleague(colleague):
    def buyStuff(self,num):
        print ("采购:买 %s" % num)
        self.mediator.execute("buy",num)
    def getNotice(self,content):
        print ("采购:接到通知--%s" % content)


class warehouseColleague(colleague):
    total=0
    threshold=100
    def setThreshold(self,threshold):
        self.threshold=threshold
    def isEnough(self):
        if self.total<self.threshold:
            print (" 仓库:警告……库存较低... ")
            self.mediator.execute("警告",self.total)
            return False
        else:
            return True
    def inc(self,num):
        self.total+=num
        print ("仓库:增加 %s" % num)
        self.mediator.execute("增加",num)
        self.isEnough()
    def dec(self,num):
        if num>self.total:
            print ("仓库:错误……库存是不够的")
        else:
            self.total-=num
            print ("仓库:减少 %s" % num)
            self.mediator.execute("减少",num)
        self.isEnough()
class salesColleague(colleague):
    def sellStuff(self,num):
        print ("销售:销售 %s" % num)
        self.mediator.execute("sell",num)
    def getNotice(self, content):
        print ("销售:获取通知--%s" % content)


# 中介者
class abstractMediator():
    purchase=""
    sales=""
    warehouse=""
    def setPurchase(self,purchase):
        self.purchase=purchase
    def setWarehouse(self,warehouse):
        self.warehouse=warehouse
    def setSales(self,sales):
        self.sales=sales
    def execute(self,content,num):
        pass
    
    
class stockMediator(abstractMediator):
    def execute(self,content,num):
        print ("中介者:获取信息--%s" % content)
        if  content=="buy":
            self.warehouse.inc(num)
            self.sales.getNotice("买 %s"%num)
        elif content=="increase":
            self.sales.getNotice("Inc %s"%num)
            self.purchase.getNotice("Inc %s"%num)
        elif content=="decrease":
            self.sales.getNotice("Dec %s"%num)
            self.purchase.getNotice("Dec %s"%num)
        elif content=="warning":
            self.sales.getNotice("库存较低.%s 左边."%num)
            self.purchase.getNotice("库存很低。请购买更多!!! %s 左边"%num)
        elif content=="sell":
            self.warehouse.dec(num)
            self.purchase.getNotice("售出 %s"%num)
        else:
            pass



if  __name__=="__main__":
    mobile_mediator=stockMediator()#先配置
    mobile_purchase=purchaseColleague(mobile_mediator)
    mobile_warehouse=warehouseColleague(mobile_mediator)
    mobile_sales=salesColleague(mobile_mediator)
    mobile_mediator.setPurchase(mobile_purchase)
    mobile_mediator.setWarehouse(mobile_warehouse)
    mobile_mediator.setSales(mobile_sales)

    mobile_warehouse.setThreshold(200)
    mobile_purchase.buyStuff(300)
    mobile_sales.sellStuff(120)













