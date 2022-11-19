
try:
    no1 = int(input("enter no 1 "))
    no2 = int(input("enter no 2 "))

    x = no1 / no2
    print(x)

    
except ZeroDivisionError:
    print("cannot divide by zero")
        
except ValueError:
        print("please enter digits only")
        
except:
        print("somethong went wrong....")        



