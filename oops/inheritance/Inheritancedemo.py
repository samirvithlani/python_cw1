#Inheritance is the capability of one class
# to derive or inherit the properties from some another class.
#inheritance  is child class can use parent class properties

#reushablity of code
#class BaseClass::
    #body of base class
#class DerivedClass(BaseClass):
   #body of derived class
   
class Person:

    name =""
    id = ""
    #constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def printPersonData(self):
        print("Name: ",self.name)
        print("Id: ",self.id)

#per = Person("amit",101)
#per.printPersonData()

class Student(Person):
   pass

class Employee(Person):
    pass
         


stu = Student("amit",101)
stu.printPersonData()         


emp = Employee("amita",102)
emp.printPersonData()
            
        