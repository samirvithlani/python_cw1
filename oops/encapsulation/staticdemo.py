class Student:
    #static variable
    #static variable is shared by all objects
    #only one copy of static variable is created
    course = "java" #class level variable
    
    #parameterized constructor
    def __init__(self,name,id):
        self.name = name                #instance level variable
        self.id = id                    #instance level variable

stu1 = Student("amit",101)
stu2 = Student("amita",102)

print(stu1.name)
print(stu1.id)
print(stu1.course)
print(stu2.name)
print(stu2.id)
print(stu2.course)        
    
#accessing static variable using class name
print("class ",Student.course)    