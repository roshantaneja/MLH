import numpy as np

#making column matrix with a traspose
x = np.array([[1,5,3]]).T
x = np.array([[1],[5],[3]])
print(x.shape)

A = np.array([[1,1,1],[1,1,1]])
B = np.array([[1,1,1],[1,1,1],[1,1,1]])
C = np.array([[1,1,1]])

test0 = A.dot(B)
print(test0.shape)

# test1 = A.dot(C) error
test1 = A.dot(C.T)
print(test1.shape)

test2 = C.dot(C.T)
print(test2.shape)