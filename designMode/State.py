"""

State 状态模式

电梯的控制逻辑，即使简单点设计，把状态分成开门状态，停止状态和运行状态，
操作分成开门、关门、运行、停止，那流程也是很复杂的。
首先，
开门状态不能开门、运行、停止；
停止状态不能关门，停止；
运行状态不能开门、关门、运行。
"""


# 实现抽象的状态类
class LiftState:
    def open(self):
        pass
    def close(self):
        pass
    def run(self):
        pass
    def stop(self):
        pass

# 具体的状态类
class OpenState(LiftState):
    def open(self):
        print ("打开:门开了……")
        return self
    def close(self):
        print ("打开:门开始关上……")
        print ("打开:门关上了")
        return StopState()
    def run(self):
        print ("打开:禁止运行。")
        return self
    def stop(self):
        print ("打开:停止被禁止的。")
        return self
class RunState(LiftState):
    def open(self):
        print ("运行:禁止打开。")
        return self
    def close(self):
        print ("运行:被禁止的。")
        return self
    def run(self):
        print ("运行:电梯正在运行…")
        return self
    def stop(self):
        print ("运行:电梯开始停止……")
        print ("运行:电梯停了下来…")
        return StopState()
class StopState(LiftState):
    def open(self):
        print ("停止:门是开的…")
        print ("停止:门开了…….")
        return OpenState()
    def close(self):
        print ("停止:关闭禁止")
        return self
    def run(self):
        print ("停止:电梯开始运行……")
        return RunState()
    def stop(self):
        print ("停止:电梯停止。")
        return self


# 将上下文进行记录
class Context:
    lift_state=""
    def getState(self):
        return self.lift_state
    def setState(self,lift_state):
        self.lift_state=lift_state
    def open(self):
        self.setState(self.lift_state.open())
    def close(self):
        self.setState(self.lift_state.close())
    def run(self):
        self.setState(self.lift_state.run())
    def stop(self):
        self.setState(self.lift_state.stop())

if __name__=="__main__":
    ctx = Context()
    ctx.setState(StopState())
    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()
















