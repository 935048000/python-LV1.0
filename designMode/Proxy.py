"""
代理模式
"""

# 构造一个网络服务器
#该服务器接受如下格式数据，addr代表地址，content代表接收的信息内容
info_struct=dict()
info_struct["addr"]=10000
info_struct["content"]=""
class Server:
    content=""
    def recv(self,info):
        pass
    def send(self,info):
        pass
    def show(self):
        pass
class infoServer(Server):
    def recv(self,info):
        self.content=info
        return "接收 OK!"
    def send(self,info):
        pass
    def show(self):
        print ("显示:%s" % self.content)

# 代理配置
"""
代理中有一个server字段，控制代理的服务器对象，infoServerProxy充当Server的直接接口代理，
而whiteInfoServerProxy直接继承了infoServerProxy对象，同时加入了white_list和对白名单的操作。
"""
class serverProxy:
    pass
class infoServerProxy(serverProxy):
    server=""
    def __init__(self,server):
        self.server=server
    def recv(self,info):
        return self.server.recv(info)
    def show(self):
        self.server.show()

class whiteInfoServerProxy(infoServerProxy):
    white_list=[]
    def recv(self,info):
        try:
            assert type(info)==dict
        except:
            return "信息结构不正确。"
        addr=info.get("addr",0)
        if not addr in self.white_list:
            return "你的地址不在白名单里。"
        else:
            content=info.get("内容","")
            return self.server.recv(content)
    def addWhite(self,addr):
        self.white_list.append(addr)
    def rmvWhite(self,addr):
        self.white_list.remove(addr)
    def clearWhite(self):
        self.white_list=[]



if  __name__=="__main__":
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"
    info_server = infoServer()
    info_server_proxy = whiteInfoServerProxy(info_server)
    print (info_server_proxy.recv (info_struct))
    info_server_proxy.show()
    info_server_proxy.addWhite(10010)
    print (info_server_proxy.recv (info_struct))
    info_server_proxy.show()








