class Base1(object):
    #str = ""
    def __init__(self):
        self.str ="Base1"
        print("Base1")
        
class Base2(object):
    #str = ""
    def __init__(self):
        self.str ="Base2"
        print("Base2")
        

class Derived(Base1,Base2):
    #derived class constructor
    
    def __init__(self):
        #calling of base1 and base2 constructor
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
        
    def printData(self):
        print(self.str,self.str)
        
dv = Derived()
dv.printData()                            
        