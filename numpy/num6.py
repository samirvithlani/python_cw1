import numpy as np

x = np.array(([1,2,3],[4,5,6]))
y = np.array(([1,2],[3,4],[5,6]))

# print(x)
# print(y)
# z = np.dot(x,y)
# print(z)

a = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(a)
b = np.linalg.det(a)
print(b)

ans = np.trace(a)
print(ans)