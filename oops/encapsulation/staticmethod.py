class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    #decorator , annotation
    
    @classmethod
    def printEmployeeData(self):
        print("print data")
        
    
    #decorator 
    @staticmethod
    def getEmployeeData():
        print("get employee data")            
        
        
emp = Employee("amit",101)
emp.printEmployeeData()
Employee.getEmployeeData()