sen = "i love india, i love gujarat"
sen = sen.capitalize()
print(sen)

message = "python i is a programming language,python is oops language cpcy"
print("index -->",message.index('is'))


x = message.count('py',6,20)
print(x)

text = "bomb is a bomb"
ans = text.endswith('bomb')
if ans:
    print("yes")
else:
    print("no")     
    
#ans ? print("yes") : print("no")

name = "1251l"

#print(name.isalpha())
#print(name.isalnum())
print(name.isnumeric())
print(name.isdigit())
    
email = "samir"    
password = "z"

#email =email.join(password)

print(email.find('a'))

#email = email.replace('i','ee')


print(email.upper())
print(email)
print(email.islower())

title = "i love india"
title = title.title()
print(title)

sentance =  "India is my country"
print(sentance.split(','))

sname = "samir"[::-1]
print(sname)