import numpy as np
i_list=[[1,0,1],[2,-1,1],[-3,2,-2]]
A=np.array(i_list)
inv_A=np.linalg.inv(A)
B=np.array([-2,1,-1])
X=np.linalg.inv(A).dot(B)
print(X)