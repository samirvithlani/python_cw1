
try:
    lang = {1:"Hindi", 2:"English", 3:"French", 4:"German"}

    print(lang[4])

except KeyError:
    print("key not found")
else:
    print("no exception")    
