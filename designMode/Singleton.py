import threading
import time
"""
单例模式
"""

#这里使用方法__new__来实现单例模式
class Singleton(object):#抽象单例
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

#总线
class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print ("发送信号数据...",data)
        self.lock.release()

#线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus=""
    name=""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)

if  __name__=="__main__":
    for i in range(3):
        print ("实体 %d 开始运行..."%i)
        my_entity=VisitEntity()
        my_entity.setName("实体_"+str(i))
        my_entity.start()