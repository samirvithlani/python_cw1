#to store data permanently we use files and to read and write data into files we use file handling
# open write/read close
#mode r read
#mode w write
#mode a append
#mode r+ read and write
#mode w+ write and read
#mode a+ append and read

def writeDataToFile():
    #open file in write mode
    file = open("demo1.txt","w")
    #check file is opend or not
    if file:
        print("file is opened")
        #write data into file
        str = "welcome to python"
        file.write(str)
        print("data is written into file")
    else:
        print("file is not opened")    
        
def appendDataToFile():
    #open file in write mode
    file = open("C:\\Users\\Samir\\Desktop\\desk1.txt","a")
    #check file is opend or not
    if file:
        print("file is opened")
        #write data into file
        str = "\n welcome to python"
        file.write(str)
        print("data is written into file")
    else:
        print("file is not opened")    
        
    file.close()
 
list =[] 
def readDataFromFile():
    
    file  = open("demo1.txt","r")
    count=0
    for i in file:
        for word in i.split():
            count+=1
            list.append(word)         
    print("no of lines in file is ",count)        
    print("no of words in file is ",list)

#writeDataToFile()        
#appendDataToFile()

#readDataFromFile()

def findPalindrome():
    strword = "naman"
    revstr = strword[::-1]
    if strword == revstr:
        print("palindrome")
    print(revstr)

findPalindrome()    