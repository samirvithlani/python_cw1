
def double(x):
    return x *2
print(double(5))

square  = lambda x: x*x
print(square(5))

#def square(x):
#    return x *x

my_list = (1,5,4,6,8,11,3,12)
even_list=[]

'''
for i in my_list:
    if i %2 == 0:
        even_list.append(i)
'''
even_list =list(filter(lambda x: (x%2 == 0), my_list))
print("even",even_list)   

studentslist = ["jay","jim","joe","jane","jill","jack"]
stutup = tuple(studentslist)     
print(stutup)

def sum(x,y):
    return x+y


ans = lambda x,y: x+y
print(ans(5,6))



ans1 = lambda p,b: p**b
print(ans1(6,3))


emp = ["raj","jay","neha","priya"]

for e in emp:
    e =e.upper()
    print(e)
    
#print(lambda x: x.upper(),emp)    

#convert list to upper case using lambda
emp1 = ["raj","jay","neha","priya"]

anns3 = map(lambda x: x.upper(),emp1)






