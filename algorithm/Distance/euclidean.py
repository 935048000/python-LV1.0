"""欧氏距离"""
import numpy as np
from scipy.spatial.distance import pdist

# 向量
# 二维
# A = np.array([1,2])
# B = np.array([1,3])

# n维
A = np.random.random (10)  # 10维
B = np.random.random (10)

print ("向量：", A, B)

# 矩阵
# A = np.mat([1,2])
# B = np.mat([1,3])


# 公式求解
d1 = np.sqrt (np.sum (np.square (A - B)))
print ("结果:", d1)

# scipy库求解
X = np.vstack ([A, B])
d2 = pdist (X)
print ("结果:", d2)

"""标准化欧氏距离"""

import numpy as np

x = np.random.random (10)
y = np.random.random (10)

X = np.vstack ([x, y])

# 方法一：根据公式求解
sk = np.var (X, axis=0, ddof=1)
d1 = np.sqrt (((x - y) ** 2 / sk).sum ())
print (d1)

# 方法二：根据scipy库求解
from scipy.spatial.distance import pdist

d2 = pdist (X, 'seuclidean')
print (d2)
