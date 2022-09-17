no = 121
tempno = no;
rem = 0
ans =0
while no!=0:
    # rem = 121 % 10 = 1
    # rem = 12 % 10 = 2
    # rem = 1 % 10 = 1
    rem = no%10
    # 0 = 0 *10 +1 ans =1
    #ans = 1 *10 + 2 = 12
    #and 12 * 10 +  1 121
    ans = ans*10 + rem
    no //=10 # 121 // 10 12 # 12 // 10 = 1 # 1 // 10 = 0
    
if ans == tempno:
    print("Palindrome")
else:
    print("Not Palindrome")
             