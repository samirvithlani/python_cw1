students = ["Johny", "Mary", "Bob", "Alice",["Tom", "Jerry"]]
#print(students[1:])
#print(students[1:2])
#print(students[:])
s = students[1]
students[1] = "mars"
print(students)
#at the end of list...push
students.append("joy")
#specific index
students.insert(3,["a","b","x","y","z"])
print(students)
#list args multipule.
students.extend(["jay","parth","neha","vedant"])
print(students)

#single delete
#del students[1]
#multipule delete
#del students[1:3]
#del students[3][1]
#deletedelm = students.pop()
#students.remove("John")
#students.clear()

print(students)
print(len(students[0]))

for i in students:
    print(i)
