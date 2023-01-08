import mysql.connector

def getallRecord():
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        sql = "select * from emp where id = %s"
        value = [8]
        cursor = myDb.cursor()
        cursor.execute(sql,value)
        result = cursor.fetchall()
        
        for x in result:
            print(x)
            
        myDb.close()    
    


def insertRecord():
    name = input("Enter name: ")
    email = input("Enter email: ")

    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        print("Connected to MySQL database")
        #%s is a placeholder for a string value
        sql ="INSERT into emp(name,email)values(%s,%s)"
        value = [name,email]
        #submit query to database using execute method
        cursor = myDb.cursor()
        cursor.execute(sql,value)
        myDb.commit()
        myDb.close()
    
    #rows count...
        if cursor.rowcount>0:
            print("Record inserted successfully")
        else:
            print("Record not inserted")
            
    else:
        print("Connection failed")    
        


def deleteRecord():
    #id = int(input("Enter id: "))
    name = input("Enter name: ")
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        print("Connected to MySQL database")
        sql = "DELETE from emp where name=%s"
        value = [name]
        curosr = myDb.cursor()
        curosr.execute(sql,value)
        myDb.commit()
        myDb.close()
        
        if curosr.rowcount>0:
            print("Record deleted successfully",curosr.rowcount)
        else:
            print("Record not deleted",curosr.rowcount)
    else:
        print("Connection failed")    
    

def updateRecord():
    mydb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    name = input("Enter name to update: ")
    email = input("Enter email to update: ")
    id = int(input("Enter id to update: "))
    sql = "update emp set name = %s, email = %s where id = %s"
    value =[name,email,id]
    cursor = mydb.cursor()
    cursor.execute(sql,value)
    mydb.commit()
    mydb.close()
    
    if cursor.rowcount>0:
        print("Record updated successfully",cursor.rowcount)
    else:
        print("Record not updated",cursor.rowcount)    
    
    


print("Enter 1 to insert record")
print("Enter 2 to delete record")
print("Enter 3 to update record")
print("Enter 4 to get all record")
choice = int(input("Enter your choice: "))
if choice == 1:
    insertRecord()
elif choice == 2:
    deleteRecord()
elif choice == 3:
    updateRecord()        
elif choice == 4:
    getallRecord()
            