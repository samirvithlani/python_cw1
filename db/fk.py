import mysql.connector

def insertEmpWithDept():
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    insertSQL = "INSERT into employee(ename,did)values(%s,%s)"
    name = input("Enter employee name: ")
    did =0
    print("press 1 for HR")
    print("press 2 for DEV")
    print("press 3 for MNG")
    choice = int(input("Enter dept id: "))
    
    if choice == 1:
        did =1
    elif choice == 2:
        did =2
    elif choice == 3:
        did =3        
        
    values = [name,did]
    cursor = myDb.cursor()
    cursor.execute(insertSQL,values)
    myDb.commit()
    myDb.close()
    
    if cursor.rowcount>0:
        print("Record inserted successfully")
    else:
        print("Record not inserted")    



def getallRecord():
    myDb = mysql.connector.connect(host="localhost",user="root",password ="root",database="cw1")
    if myDb:
        sql = "select * from employee natural join dept"
        value = [8]
        cursor = myDb.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        
        print("id\tename\tdid\tdeptname")
        for x in result:
            print(x)
            
        myDb.close()    
    


#insertEmpWithDept()    
getallRecord()