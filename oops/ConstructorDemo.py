#constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the
# class when an object of class is created
# .In Python the __init__() method is called the constructor and is always
# called when an object is created.
#types of constructor
#default constructor
# the defaulr constructor is simple constructor which doesn't accept any arguments.
# it's definition has only one argument which is a reference to the instance being (self)

#parameterized constructor
#constructor with parameters is known as parameterized constructor.
#the parameterized constructor take its first argument as a reference to the current instance of the class,(self)
# and the rest of the arguments are provided by the programmer.


class Employee:
     #default constructor

     eId=0    
     
     def __init__(self):
         self.eId = 100
         print("default constructor")
         
     def employeeData(self):
         print("Employee Id: ",self.eId)    
    
     
          
     def __init__(self,eId):
         print("parameterized constructor")
         self.eId = eId
         
     def __init__(self,eId,eName):
         print("parameterized constructor")
         print("Employee Id: ",eId)
         print("Employee Name: ",eName)      

#default constructor will call
#emp = Employee(150)
emp = Employee(150,"amit")
emp.employeeData()
         
