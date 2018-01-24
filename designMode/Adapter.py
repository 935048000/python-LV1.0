
"""
适配器模式
"""


class ACpnStaff:
    name=""
    id=""
    phone=""
    def __init__(self,id):
        self.id=id
    def getName(self):
        print ("A 协议getName方法id:%s" % self.id)
        return self.name
    def setName(self,name):
        print ("A 协议setName方法id:%s" % self.id)
        self.name=name
    def getPhone(self):
        print ("A 协议getPhone方法id:%s" % self.id)
        return self.phone
    def setPhone(self,phone):
        print ("A 协议setPhone方法id:%s" % self.id)
        self.phone=phone
class BCpnStaff:
    name=""
    id=""
    telephone=""
    def __init__(self,id):
        self.id=id
    def get_name(self):
        print ("B 协议get_name方法id:%s" % self.id)
        return self.name
    def set_name(self,name):
        print ("B 协议setName方法id:%s" % self.id)
        self.name=name
    def get_telephone(self):
        print ("B 协议get_telephone方法id:%s" % self.id)
        return self.telephone
    def set_telephone(self,telephone):
        print ("B 协议get_name方法id:%s" % self.id)
        self.telephone=telephone

# 适配器
class CpnStaffAdapter:
    b_cpn=""
    def __init__(self,id):
        self.b_cpn=BCpnStaff(id)
    def getName(self):
        return self.b_cpn.get_name()
    def getPhone(self):
        return self.b_cpn.get_telephone()
    def setName(self,name):
        self.b_cpn.set_name(name)
    def setPhone(self,phone):
        self.b_cpn.set_telephone(phone)



if __name__=="__main__":
    acpn_staff=ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print ("A 员工的名字:%s" % acpn_staff.getName ())
    print ("A 工作人员电话:%s" % acpn_staff.getPhone ())
    bcpn_staff=CpnStaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print ("B 员工的名字:%s" % bcpn_staff.getName ())
    print ("B 工作人员电话:%s" % bcpn_staff.getPhone ())
    