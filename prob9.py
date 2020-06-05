import numpy as np
a=np.array([[2, 1],[1, 0], [0, 1]])
s1=np.linalg.svd(a)[1]
#usv=np.linalg.svd(a)
print('Singular values for the first matrix:\n',s1)#, np.linalg(a))
b=np.array([[1,1,0],[1,0,1],[0,1,1]])
s2=np.linalg.svd(b)[1]
print('Singular values for the second matrix:\n',s2)
