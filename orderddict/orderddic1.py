from collections import OrderedDict
# blank dictionary
d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
d1['d'] = 4


'''
for key,value in d1.items():
    print(key,value)
'''

print("\n\n")
for i in d1:
    print(i,d1[i])


d1['c'] = 5
print("after....")
for i in d1:
    print(i,d1[i])

od = OrderedDict()
od['c']=1
od['a']=2
od['p']=100
od['l']=20
od['a']=120
for key,value in od.items():
    print(key,value)


    