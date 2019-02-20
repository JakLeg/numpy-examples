import numpy as np

# creating a vector of size 10 all with 0's

Z = np.zeros(10)
print(Z)

# creating a matrix of size 10x10 with all 0's

Z  = np.zeros((10, 10))
print(Z)

# creating a matrix of size 10x10 with 1's

O = np.ones((10,10))
print(O)

# creating a matrix with random numbers

R = np.random.random((10, 10))
print(R)

# creating a matrix with gaussian random numbers

G = np.random.randn(10,10) # mean = 0, variance = 1
print(G)

