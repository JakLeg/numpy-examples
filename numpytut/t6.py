import numpy as np

# matrix product

# '*' means: element by element multiplication
# '.dot()' means: matrix multiplication

M1 = np.random.random((5, 5))
M2 = np.random.random((5, 5))

print(M1.dot(M2))
print('-=-' * 15)
print(M1 * M2)
