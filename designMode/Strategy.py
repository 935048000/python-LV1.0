
"""

策略模式

假设某司维护着一些客户资料，需要在该司有新产品上市或者举行新活动时通知客户。
通知客户的方式有两种：短信通知、邮件通知。
应如何设计该系统的客户通知部分？
为解决该问题，我们先构造客户类，包括客户常用的联系方式和基本信息，同时也包括要发送的内容。
"""
class customer:
    customer_name=""
    snd_way=""
    info=""
    phone=""
    email=""
    def setPhone(self,phone):
        self.phone=phone
    def setEmail(self,mail):
        self.email=mail
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email
    def setInfo(self,info):
        self.info=info
    def setName(self,name):
        self.customer_name=name
    def setBrdWay(self,snd_way):
        self.snd_way=snd_way
    def sndMsg(self):
        self.snd_way.send(self.info)

# 发送方式构建
class msgSender:
    dst_code=""
    def setCode(self,code):
        self.dst_code=code
    def send(self,info):
        pass
class emailSender(msgSender):
    def send(self,info):
        print ("电子邮件地址:%s 电子邮件:%s" % (self.dst_code, info))


class textSender(msgSender):
    def send(self,info):
        print ("文本:%s 电子邮件:%s" % (self.dst_code, info))


if  __name__=="__main__":
    customer_x=customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("欢迎参加我们的新晚会!")
    text_sender=textSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()
    mail_sender=emailSender()
    mail_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(mail_sender)
    customer_x.sndMsg()








