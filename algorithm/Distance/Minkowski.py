"""闵氏距离"""

import numpy as np

x = np.random.random (10)
y = np.random.random (10)

# 方法一：根据公式求解,p=2
d1 = np.sqrt (np.sum (np.square (x - y)))
print (d1)

# 方法二：根据scipy库求解
from scipy.spatial.distance import pdist

X = np.vstack ([x, y])
d2 = pdist (X, 'minkowski', p=2)
print (d2)
