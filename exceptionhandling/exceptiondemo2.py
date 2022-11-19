try:
    no1 = int(input("enter no 1 "))
    #//50 files open   46 th location  46 exception 45 open... terminate...
    #//45 still open data leak
    #connection close..
    #class --> destroy --> null  ->

except:
    print("something went wrong")
else:
    print("no exception")
        
finally:
    print("finally block")    

 
