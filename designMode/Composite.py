"""

组合模式
"""


# 树形的公司结构
class Company:
    name = ''
    def __init__(self, name):
        self.name = name
    def add(self, company):
        pass
    def remove(self, company):
        pass
    def display(self, depth):
        pass
    def listDuty(self):
        pass

class ConcreteCompany(Company):
    childrenCompany = None
    def __init__(self, name):
        Company.__init__(self,name)
        self.childrenCompany = []
    def add(self, company):
        self.childrenCompany.append(company)
    def remove(self, company):
        self.childrenCompany.remove(company)
    def display(self, depth):
        print ('-' * depth + self.name)
        for component in self.childrenCompany:
            component.display(depth+1)
    def listDuty(self):
        for component in self.childrenCompany:
            component.listDuty()
class HRDepartment(Company):
    def __init__(self, name):
         Company.__init__(self,name)
    def display(self, depth):
        print ('-' * depth + self.name)

    def listDuty(self): #履行职责
        print ('%s\t 过户登记和管理.' % self.name)


class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self,name)
    def display(self, depth):
        print ("-" * depth + self.name)

    def listDuty(self): #履行职责
        print ('%s\t财务管理.' % self.name)


class RdDepartment(Company):
    def __init__(self,name):
        Company.__init__(self,name)
    def display(self, depth):
        print ("-" * depth + self.name)

    def listDuty(self):
        print ("%s\t研发." % self.name)



# 总公司下设东边的分公司一个，东边的分公司下设东北公司和东南公司，
# 显示公司层级，并罗列这些的公司中各部门的职责，
if __name__=="__main__":
    root = ConcreteCompany('总公司')
    root.add(HRDepartment('总部人力资源'))
    root.add(FinanceDepartment('总部财务'))
    root.add(RdDepartment("总部研发"))

    comp = ConcreteCompany('东边分公司')
    comp.add(HRDepartment('东边分公司。人力资源'))
    comp.add(FinanceDepartment('东边分公司.财政'))
    comp.add(RdDepartment("东边分公司.研发"))
    root.add(comp)

    comp1 = ConcreteCompany('东北 分公司')
    comp1.add(HRDepartment('东北.人力资源'))
    comp1.add(FinanceDepartment('东北.财政'))
    comp1.add(RdDepartment("东北.研发"))
    comp.add(comp1)

    comp2 = ConcreteCompany('东南 分公司')
    comp2.add(HRDepartment('东南.人力资源'))
    comp2.add(FinanceDepartment('东南.财政'))
    comp2.add(RdDepartment("东南.研发"))
    comp.add(comp2)

    root.display(1)

    root.listDuty()
























