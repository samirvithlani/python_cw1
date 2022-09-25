users =[{"id":1,"name":"tom","age":20,"salary":10000},{"id":2,"name":"jerry","age":30,"salary":20000},{"id":3,"name":"lucy","age":40,"salary":30000}]
print(users)

for i in users:
    print(i.keys()," - ",i.values())
    
    
users1 = {1:{"id":1,"name":"tom","age":20,"salary":10000},2:{"id":2,"name":"jerry","age":30,"salary":20000},3:{"id":3,"name":"lucy","age":40,"salary":30000}}
print(users1)

for i in users1:
    print(i," - ",users1[i])