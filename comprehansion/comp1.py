data = [1,2,3,4,5,6,7,8,9,10,45,89,75,25,96,32,45,63,25,22,14,20]
evenlist =[]


# for i in data:
#     if i %2 ==0 and i >=10:
#         evenlist.append(i)


evenlist = [i for i in data if i %2 ==0 and i >=10]
print(evenlist)        