#argv argumet variable
#* wild card char...

from re import L


def demo(name,age):
    print(name,age)
    
def getNames(*argv):
    for name in argv:
        return argv
    
def getNames2(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])
    


print(getNames("jhon", "jane", "joe", "jim"))
demo("joe", 45)

getNames2(name="joe", age=45, address="123 main st", city="atlanta")
    
    
    

