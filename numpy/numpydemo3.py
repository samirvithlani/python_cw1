import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
#print(a+1)
 

print(a.sum(axis=0))
print(a.sum(axis=1))
print(a * b)
print(a.sum() + b.sum())
#print((a+b).sum())
print("transpose....",np.transpose(a))
#axis=0 means column
#axis=1 means row