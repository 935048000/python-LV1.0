"""

观察者模式

从业务流程的实现角度，实现该火警报警器。
"""


# class AlarmSensor:
#     def run(self):
#         print ("报警器...")
#
#
# class WaterSprinker:
#     def run(self):
#         print ("洒水器...")
#
#
# class EmergencyDialer:
#     def run(self):
#         print ("拨 119...")


# 将三个类提取共性，泛化出“观察者”类，并构造被观察者。
class Observer:
    def update(self):
        pass


class AlarmSensor (Observer):
    def update(self, action):
        print ("收到报警: %s" % action)
        self.runAlarm ()
    
    def runAlarm(self):
        print ("报警器...")


class WaterSprinker (Observer):
    def update(self, action):
        print ("收到洒水: %s" % action)
        self.runSprinker ()
    
    def runSprinker(self):
        print ("洒水器...")


class EmergencyDialer (Observer):
    def update(self, action):
        print ("收到拨号: %s" % action)
        self.runDialer ()
    
    def runDialer(self):
        print ("拨 119...")


# 被观察者
class Observed:
    observers=[]
    action=""
    def addObserver(self,observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)
class smokeSensor(Observed):
    def setAction(self,action):
        self.action=action
    def isFire(self):
        return True


if __name__=="__main__":
    alarm=AlarmSensor()
    sprinker=WaterSprinker()
    dialer=EmergencyDialer()

    smoke_sensor=smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)


    if smoke_sensor.isFire():
        smoke_sensor.setAction("着火!")
        smoke_sensor.notifyAll()
















