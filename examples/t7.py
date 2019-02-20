import numpy as np

# matrix operations with numpy
A = np.array([[1,2][3,4]])
print(A)

# inverse matrix
Ainv = np.linalg.inv(A)
print(Ainv)

# multiplying
print(' A x Ainv = ', Ainv.dot(A))

# determinant
print(np.linalg.det(A))

# main diagonal
print(np.diag(A)) # [1,4]

# filling the second diagonal with 0's
print(np.diag([1,2]))

###

a = np.array([1,2])
b = np.array([3,4])

# outer product
print(np.outer(a,b))

# inner product // same as dot product
print(np.inner(a, b))

###

# sum of matrix diagonal

print(np.diag(A).sum())
# or
print(np.tace(A))

########

X np.random.randn(100, 3)

cov = np.cov(X)

# shape (matrix dimensions)
print(cov.shape) # 100 x 3

cov = np.cov(X.T)

print(cov)

# EIGEN VALUES AND EIGEN VECTORS

np.linalg.eigh(cov)

