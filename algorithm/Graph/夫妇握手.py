"""

N对夫妇坐在连续排列的2N个座位上，想要牵手。我们想知道交换的最低数量，以便每对夫妻并肩坐在一起。
一个交换包括选择的任何两个人，然后他们站起来交换座位。
人民和座椅由一个整数表示0到2N-1时，情侣们在顺序编号，
第一对夫妇之中(0, 1)，第二夫妇之中(2, 3)，所以与过去几个是(2N-2, 2N-1)。
夫妻最初的座位是row[i]作为最初坐在第一位的人的价值给出的。

"""


def minSwapsCouples(row):
    res = 0
    # i为位置
    # p为另一半
    for i in range (0, len (row), 2):
        # 如果i位置的人是2N-2 ，则另一半等于2N-1（i位置的人+1）
        if row[i] % 2 == 0:
            p = row[i] + 1
        # 否则i位置的人是2N-1 ，则另一半等于2N-2（i位置的人-1）
        else:
            p = row[i] - 1
        
        # j 等于另一半的位置
        j = row.index (p)
        
        # 如果 另一半的位置与当前人位置 差距大于1，则把另一半的位置调到当前位置的后面（i+1）
        if j - i > 1:
            row[i + 1], row[j] = row[j], row[i + 1]
            # 调动次数加1
            res += 1
            
    return res


print(minSwapsCouples([3, 2, 0, 1]))

