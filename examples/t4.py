import numpy as np

# matrix in normal python

L = [[1,2],[3,4]]

# arrays in numpy

M = np.array([[1,2],[3,4]])

# ways to acces the elements

print(M[0][0]) # 1

# OR

print(M[0,0]) # 1

# Matrix in numpy

M2 = np.matrix([[1,2], [3,4]])

# transforming matrix to array

A = np.array(M2)

# transpose

print(A.T)

