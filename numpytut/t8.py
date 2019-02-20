import numpy as np

# solving linear system

# proble Ax = b
# AinvAx = x = Ainvb

A = np.array([[1,2],[3,4]])
b = np.array([1,2])

# A = ([1,2],
#      [3,4])

# b = ([1,2])

x = np.linalg.inv(A).dot(b)

print(x) # solution

# or you can just do this

print(np.linalg.solve(A, b))
