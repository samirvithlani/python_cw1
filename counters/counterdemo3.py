from collections import Counter

c1 = Counter(a=3,b=6,c=12)
c2 = Counter(a=1,b=2,c=3)

c2.subtract(c1)
print(c2)
