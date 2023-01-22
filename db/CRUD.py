import mysql.connector

def insertStudent():
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        print("Connected to MySQL database")
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        age = int(input("Enter student age: "))
        
        #%s place holder....
        insertSQL = "INSERT into students(name,email,age)values(%s,%s,%s)"
        values =[name,email,age]
        cursor = myDb.cursor()
        cursor.execute(insertSQL,values)
        myDb.commit()
        myDb.close()
        
        if cursor.rowcount>0:
            print("Record inserted successfully")
        else:
            print("Record not inserted")    


def getAllRecords():
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        print("Connected to MySQL database")
        SELECTSQL = "SELECT * from students where name = %s"
        values = ["raja"]
        cursor = myDb.cursor()
        cursor.execute(SELECTSQL,values)
        res = cursor.fetchall()  
        print(res)         
        myDb.close()

def updateStudent():
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        print("Connected to MySQL database")
        
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        age = int(input("Enter student age: "))
        id = int(input("Enter student id: "))
        updateSQL = "UPDATE students set name = %s,email = %s,age = %s where id = %s"
        values =[name,email,age,id]
        cursor = myDb.cursor()
        cursor.execute(updateSQL,values)
        myDb.commit()
        myDb.close()
        
        if cursor.rowcount>0:
            print("Record updated successfully")
        else:
            print("Record not updated")    
            
# insertStudent()    
#getAllRecords()
updateStudent()