from collections import Counter

conn = Counter()
conn.update([1,2,3,1,2,1,1,2])
print(conn)
conn.update([1,2,3])
print(conn)

c1 =["jay","raj","amit"]
c2 = ["jay","neha","akshay","amit"]

conn1 = Counter()
conn1.update(c1)
conn1.update(c2)
print(conn1)