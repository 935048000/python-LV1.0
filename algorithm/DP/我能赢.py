"""


在“100个游戏”中，两个玩家轮流添加，一个运行的总数，任何整数从1..10。首先导致总跑次数达到或超过100胜的选手。
如果我们改变游戏，让玩家不能重新使用整数会怎样?例如，两个玩家可能会轮流从一个普通的1。
15不替换，直到它们达到>= 100。
给定一个整数maxChoosableInteger和另一个整数desiredTotal，确定第一个移动的玩家是否可以强制一个win，
假设这两个玩家都是最优的。
你可以一直假设maxChoosableInteger不会是lar。

"""

class Solution:
    # 自上而下的DFS：时间：O（N * 2 ^ N）。空间：O（2 ^ N）
    def helper(self, allowed, target, so_far, cache):
        # allowed值的长度范围为1到maxChoosableInteger（N）
        if len (allowed) == 0:
            return False
        state = tuple (allowed)
        if state in cache:
            return cache[state]
        else:
            cache[state] = False
            # 赢了
            if max (allowed) + so_far >= target:
                cache[state] = True
            # 否则从所允许的值中逐一选择并递归调用另一个玩家。
            else:
                for x in allowed:
                    new_allowed = [y for y in allowed if x != y]
                    if self.helper (new_allowed, target, so_far + x, cache) == False:
                        cache[state] = True
                        break
            return cache[state]
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        allowed = [x for x in range (1, maxChoosableInteger + 1)]
        # 测试输入是否有效
        if sum (allowed) < desiredTotal:
            return False
        
        return self.helper (allowed, desiredTotal, 0, {})


a = Solution()
print(a.canIWin(10,11))








