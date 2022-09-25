#set is unorderd collection of unique items
#set is mutable
#set follows hash table concept
# {} is used to create set
#[] ,() ,{"":""},{}

colors = {'red', 'green', 'blue', 'yellow', 'red'}
colors.add('black')
for i in colors:
    print(i)
len = len(colors)
print(len)


#colors.clear()
#print("removing...",colors.pop())



#colors.remove('red')
#colors.update(["white","pink"])
#colors.update(("white","pink"))
colors.update({"white":"pink"})
print("-----",colors)



country = {'india', 'usa', 'uk', 'china', 'japan'}
state = {'karnataka', 'tamilnadu', 'kerala', 'karnataka', 'tamilnadu','india'}
city = {'bangalore', 'chennai', 'mumbai', 'delhi', 'bangalore','india'}

#data = country.union(state).union(city)
data = country | state | city
print(data)


#data1 = country.intersection(state).intersection(city)
data1 = country & state & city
print(data1)


#diff = city.difference(country)
diff = city - country
print(diff)


s1 = {'a', 'b', 'c', 'd'}
s2 = {'d', 'b', 'c', 'a'}


if s1 == s2:
    print('s1 and s2 are equal')
else:
    print('s1 and s2 are not equal')    









