class Employee:
    
    email = "samir@gmail.com"
    
    def __init__(self,name,id):
        self.name = name #instance variable
        self.id = id
    
    #decorator , annotation
    
    def demo(self):
        print(self.name)
        print(self.id)
    
    @classmethod
    def printEmployeeData(self,name):
        print(name)
        print("print data",self.email)
        #print("print data",self.name)
        
    
    #decorator 
    @staticmethod
    def getEmployeeData(email):
        print(email)
        #only static variable can be used in static method
        #print(self.name)
        print("get employee data")            
        
        
emp = Employee("amit",101)
emp.printEmployeeData("mmmmm")
#emp.demo()
#Employee.getEmployeeData("samir123")