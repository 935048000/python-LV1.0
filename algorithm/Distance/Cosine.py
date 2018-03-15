"""余弦距离"""

import numpy as np
from scipy.spatial.distance import pdist

x = np.random.random (10)
y = np.random.random (10)

# solution1
dist1 = 1 - np.dot (x, y) / (np.linalg.norm (x) * np.linalg.norm (y))

# solution2
dist2 = pdist (np.vstack ([x, y]), 'cosine')

print ('x', x)
print ('y', y)
print ('dist1', dist1)
print ('dist2', dist2)
