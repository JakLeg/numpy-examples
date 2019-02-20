import numpy as np

#####################################

# dot product (return scalar)


a = np.array([1,2])
b = np.array([2,1])

dot = 0

for e, f in zip(a, b):
    dot += e*f

print(dot) # 4

print(a*b) # array([2,2])

print(np.sum(a*b)) # 4

# or you can just do:

print(np.dot(a*b)) # 4


#####################################

# magnitude

amag = np.sqrt((a*a).sum())

print(amag) # 2.23606...

# or you can just do:
amag = np.linalg.norm(a)

print(amag) # 2.23606...

# cosine of an angle

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(cosangle) # 0.79999...

angle = np.arccos(cosangle)

print(angle) # 0.643501...
