list1 =[1,2,3,4,5,6,7,8,9,10]

dic1 ={}

# for i in list1:
#     if i %2==0:
#         dic1[i] = i**2
        
        
dic1 = {i*2:i**2 for i in list1 if i%2==0}       
print(dic1)        
        

