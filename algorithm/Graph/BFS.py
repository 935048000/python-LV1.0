"""

广度优先搜索
"""


def slidingPuzzle(self, board):
    state = "".join ([str (n) for row in board for n in row])
    ans = "123450"
    if state == ans:
        return 0
    
    mem = set ()
    mem.add (state)
    # remember steps count in the queue
    queue = [(state, 0)]
    
    # 指定四个交换条件
    conditions = [
        (lambda x: x - 1 >= 0 and x != 3, -1),
        (lambda x: x - 3 >= 0, -3),
        (lambda x: x + 1 < 6 and x != 2, 1),
        (lambda x: x + 3 < 6, 3)]

    conditions = [
        # 不是最左，然后允许左。
        (lambda x: x != 0 and x != 3, -1),
        # 不是第一排，然后允许。
        (lambda x: x // 3 == 1, -3),
        # 不是最正确的，然后允许正确的。
        (lambda x: x != 2 and x != 5, 1),
        # 不是下一排，然后允许下。
        (lambda x: x // 3 == 0, 3)]
    
    while queue:
        state, step = queue.pop (0)
        zp = state.find ('0')
        for c in conditions:
            if c[0] (zp):
                # swap
                nstate = [s for s in state]
                nstate[zp], nstate[zp + c[1]] = nstate[zp + c[1]], nstate[zp]
                nstate = "".join (nstate)
                
                if nstate == ans:
                    return step + 1
                if nstate not in mem:
                    mem.add (nstate)
                    queue.append ((nstate, step + 1))
    return -1


















