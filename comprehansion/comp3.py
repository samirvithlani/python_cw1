matrix =[]
matrix1 =[]
#[]
for i in range(5):
    #i = 0
    #i = 1
    matrix.append([])
    
    #0
    for j in range(1,6):
        matrix[i].append(j)
        
print(matrix)        

#comprehension
matrix1 = [ [j for i in range(5)] for j in range(1,6)]
print(matrix1)