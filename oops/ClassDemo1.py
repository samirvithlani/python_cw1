#class name starts WIith cap
class Student:
    #instance variable  
    no= 100
    sName=""
    sAge=0
    
    def getStudentData(self):
         sName = "amit"
         print("Student Name: ",sName)
        #local variable of getStudentData function
         print(self)
         #globals()['sName'] = input("Enter Student Name: ")
         #globals()['sAge'] =  int(input("Enter Student Age: "))
         self.sName = input("Enter Student Name: ")
         self.sAge =  int(input("Enter Student Age: "))
    
    def printStudentData(self):
        #accessing instance variable
        
        #print("Student Name: ",globals()['sName'])
        #print("Student Age: ",globals()['sAge'])
        print("Student Name: ",self.sName)
        print("Student Age: ",self.sAge)
    


#create object
#s is an object of class
#property of class can not use directly out side of class
s = Student()
s1 = Student()

print(s.no)
s.getStudentData()
s1.printStudentData()


    