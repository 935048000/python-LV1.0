"""

访问者模式

假设一个药房，有一些大夫，一个药品划价员和一个药房管理员，它们通过一个药房管理系统组织工作流程。
大夫开出药方后，药品划价员确定药品是否正常，价格是否正确；
通过后药房管理员进行开药处理。
"""

# 构造药品类和工作人员类
class Medicine:
    name=""
    price=0.0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def accept(self,visitor):
        pass
    
    
class Antibiotic(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
        
        
class Coldrex(Medicine):
    def accept(self,visitor):
        visitor.visit(self)


# 抗生素和感冒药
class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
    
    
class Charger(Visitor):
    def visit(self,medicine):
        print ("收费: %s 列出了药 %s. 价格:%s " \
               % (self.name, medicine.getName (), medicine.getPrice ()))


class Pharmacy(Visitor):
    def visit(self,medicine):
        print ("医生:%s 列出了药 %s. 价格:%s" \
               % (self.name, medicine.getName (), medicine.getPrice ()))


# 药方类的构建
class ObjectStructure:
    pass
class Prescription(ObjectStructure):
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)
    def visit(self,visitor):
        for medc in self.medicines:
            medc.accept(visitor)


if __name__=="__main__":
    yinqiao_pill=Coldrex("Yinqiao Pill",2.0)
    penicillin=Antibiotic("Penicillin",3.0)
    doctor_prsrp=Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
    charger=Charger()
    charger.setName("Doctor Strange")
    pharmacy=Pharmacy()
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)













