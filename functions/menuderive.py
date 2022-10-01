def sum(a,b):
    return  a + b


def sub(a,b):
    return a - b

def div(a,b):
    c = a / b
    print("div = ",c)
    
def mul():
    a = int(input("enter no1 "))
    b = int(input("enter no2 "))
    c = a * b
    print("mul = ",c)
   
choice =0    
while(True):
    print("Press 1 for add : ")
    print("Press 2 for mul : ")
    print("Press 3 for div : ")
    print("Press 4 for sub : ")    
    print("Press 5 for exit : ")
    
    choice = int(input("Enter Choice ::"))
    if choice==1:
        a = int(input("enter no1 "))
        b = int(input("enter no2 "))
        ans = sum(a,b)
        print("ans = ",ans)
    elif choice==2:
        mul()
    elif choice ==5:
        print("Thanks ....exiting..")
        break
    else:
        print("invalid choice")   
        break
            
    
    
    
    
            