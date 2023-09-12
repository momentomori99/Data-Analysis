import numpy as np

v = np.array([1, 2, 3, 4])

b = np.array([0, 0.5, 1, 1.5, 2])

print(v[0:])
print(v[1:3])
print(v[1:-1])
print(v[::2])

print(v.dtype)
print(b.dtype)

c = np.array([1, 2, 3, 4], dtype=np.float)
print(c.dtype)

d = np.array([1, 2, 3, 4], dtype=np.int8)
print(d.dtype)



"""
Dimensions and shapes, and matrices
"""

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
print(A.ndim)
print(A.size)

"""
Indexing and slizing matrices
"""

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(A)
#print(A[0:2])
print(A[:, :2]) #meaning selecting all rows, but up to the second column
print(A[:2,2:])


"""
Some statistics
"""
# A.sum
# A.mean
# A.std

# A.sum(axis=0)
# A.mean(axis=1)
