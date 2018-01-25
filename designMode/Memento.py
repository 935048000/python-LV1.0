"""

Memento
备忘录模式

大多数游戏都有保存进度的功能
保存在内存中来模拟实现该场景的情形
"""

# 模拟一个战斗角色,创建游戏角色
import random


class GameCharacter():
    """GameCharacter定义了基本的生命值、攻击值、防御值以及实现角色状态控制的方法"""
    vitality = 0
    attack = 0
    defense = 0
    def displayState(self):
        print ('当前值:')
        print ('生命:%d' % self.vitality)
        print ('攻击:%d' % self.attack)
        print ('防御:%d' % self.defense)

    def initState(self,vitality,attack,defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
    def saveState(self):
        return Memento(self.vitality, self.attack, self.defense)
    def recoverState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense
class FightCharactor(GameCharacter):
    """FightCharactor实现具体的“战斗”接口。"""
    def fight(self):
        self.vitality -= random.randint(1,10)


# 备忘录，来保存进度
class Memento:
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense


if __name__=="__main__":
    game_chrctr = FightCharactor()
    game_chrctr.initState(100,79,60)
    game_chrctr.displayState()
    
    memento = game_chrctr.saveState()
    
    game_chrctr.fight()
    game_chrctr.displayState()
    
    # 保存进度
    game_chrctr.recoverState(memento)
    
    game_chrctr.displayState()



