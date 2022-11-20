from collections import ChainMap

c1 = {"a":1,"b":2}
c2 = {"c":3,"d":4}
c3 = {"e":5,"f":6}

c = ChainMap(c1,c2,c3)
print(c)
print(c.maps)
print(tuple(c.keys()))
print(list(c.values()))