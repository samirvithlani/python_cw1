sales = [[100,200],[250,362],[400,560],[785,562],[1000,800],[1200,1000],[1450,1780]]
totalsales =[]
sum1=0
for i in sales:
    for j in i:
        sum1 = sum1 +j
    totalsales.append(sum1)    
    sum1 =0    

maxfromlist = max(totalsales)
pos = totalsales.index(maxfromlist)
print(pos+1)
