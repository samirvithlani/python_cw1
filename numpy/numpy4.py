import numpy as np
# nums = np.arange(2.0,9.0,2)
# print(nums)

#zeros = np.zeros(5)
# zeros = np.zeros((3,3))
# print(zeros)
# onse = np.ones(5)
# print(onse)

#0
# 100 - 1 / 4 = 24.75
#
lin = np.linspace(1,100,5)
print("lin",lin)

# idn = np.eye(4)
# print(idn)

random = np.random.rand(3,4)
random = np.random.randint(1,1000,size=(3,4))
random3 = np.random.randn(3,4)
print(random)
print(random3)

random4 = np.random.randint(1,1000,5)
print(random4)
mindata = random4.min()
print(mindata)
maxdata = random4.max()
print(maxdata)

random4.sort()
print(random4)