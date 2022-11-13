#private variable can useed in same class only
class Toy:
    __price =2500 # private variable
    name = "car" # public variable
    
    #private method
    #private method can be used in same class only
    def __printPrice(self):
        print("price is ",self.__price)
    
    #public method
    def getPrice(self):
        return self.__price
    
    #Public method
    #param price
    def setPrice(self,price):
        self.__price = price
    
t  = Toy()
#print(Toy.price)    
#t.__printPrice() error

t.setPrice(4500)

x = t.getPrice()
print("price ==",x)
print(t.name)
