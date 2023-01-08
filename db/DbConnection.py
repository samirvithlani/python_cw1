import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password = "root",database="cw1")

if mydb.is_connected():
    print("Connected to MySQL database")
    cursor = mydb.cursor()
    #//create table if not exists student (id int(10) primary key, name varchar(20), age int(10))
    #cursor.execute("create table  student  (id int(10) primary key, name varchar(20), age int(10))")
    for x in cursor:
        print(x)
    
else:
    print("Connection failed")    
    