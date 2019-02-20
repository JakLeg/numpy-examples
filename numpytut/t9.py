import numpy as np


# x + y = 2200
# 1.5x + 4y = 5050
#
# also can be written as
#
# ( 1    1) (x) = (2200) 
# ( 1.5  4) (y)   (5050)

A = np.array([[1,1], [1.5, 4]])
b = np.array([2200, 5050])

print(np.linalg.solve(A, b)) # solution

