"""

命令模式

饭店有凉菜间、热菜间、主食间，那当服务员将菜品录入到系统中后，
凉菜间会打印出顾客所点的凉菜条目，热菜间会打印出顾客所点的热菜条目，主食间会打印出主食条目。
系统设计成前台服务员系统和后台系统，后台系统进一步细分成主食子系统，凉菜子系统，热菜子系统。
"""


# 后台三个子系统设计
class backSys ():
    def cook(self, dish):
        pass


class mainFoodSys (backSys):
    def cook(self, dish):
        print ("主食:烹调 %s" % dish)


class coolDishSys (backSys):
    def cook(self, dish):
        print ("冷菜:烹调 %s" % dish)


class hotDishSys (backSys):
    def cook(self, dish):
        print ("热菜:烹调 %s" % dish)


# 前台系统构建
class waiterSys ():
    menu_map = dict ()
    commandList = []
    
    def setOrder(self, command):
        print ("服务员:加菜")
        self.commandList.append (command)
    
    def cancelOrder(self, command):
        print ("服务员:撤销指令...")
        self.commandList.remove (command)
    
    def notify(self):
        print ("服务员:修改...")
        for command in self.commandList:
            command.execute ()


# 命令类构建
class Command ():
    receiver = None
    
    def __init__(self, receiver):
        self.receiver = receiver
    
    def execute(self):
        pass


class foodCommand (Command):
    dish = ""
    
    def __init__(self, receiver, dish):
        super ().__init__ (receiver)
        self.receiver = receiver
        self.dish = dish
    
    def execute(self):
        self.receiver.cook (self.dish)


class mainFoodCommand (foodCommand):
    pass


class coolDishCommand (foodCommand):
    pass


class hotDishCommand (foodCommand):
    pass



# 菜单类
class menuAll:
    menu_map=dict()
    def loadMenu(self):#加载菜单，这里直接写死
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]
    def isHot(self,dish):
        if dish in self.menu_map["hot"]:
            return True
        return False
    def isCool(self,dish):
        if dish in self.menu_map["cool"]:
            return True
        return False
    def isMain(self,dish):
        if dish in self.menu_map["main"]:
            return True
        return False





if  __name__=="__main__":
    dish_list=["Yu-Shiang Shredded Pork","Sauteed Tofu, Home Style","Cucumber","Rice"]#顾客点的菜
    waiter_sys=waiterSys()
    main_food_sys=mainFoodSys()
    cool_dish_sys=coolDishSys()
    hot_dish_sys=hotDishSys()
    menu=menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isCool(dish):
            cmd=coolDishCommand(cool_dish_sys,dish)
        elif menu.isHot(dish):
            cmd=hotDishCommand(hot_dish_sys,dish)
        elif menu.isMain(dish):
            cmd=mainFoodCommand(main_food_sys,dish)
        else:
            continue
        waiter_sys.setOrder(cmd)
    waiter_sys.notify()









