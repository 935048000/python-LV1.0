"""

门面模式
"""
# 一组火警报警系统，由三个子元件构成：一个警报器，一个喷水器，一个自动拨打电话的装置。
class AlarmSensor:
    def run(self):
        print ("报警环...")


class WaterSprinker:
    def run(self):
        print ("喷水...")


class EmergencyDialer:
    def run(self):
        print ("拨号 119...")


# 设计模式中，被封装成的新对象，叫做门面。
class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor=AlarmSensor()
        self.water_sprinker=WaterSprinker()
        self.emergency_dialer=EmergencyDialer()
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()



if __name__=="__main__":
    alarm_sensor=AlarmSensor()
    water_sprinker=WaterSprinker()
    emergency_dialer=EmergencyDialer()
    alarm_sensor.run()
    water_sprinker.run()
    emergency_dialer.run()
    print()
    emergency_facade=EmergencyFacade()
    emergency_facade.runAll()

#

























