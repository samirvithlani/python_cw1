country = ["India", "China", "Japan", "USA", "UK", "Russia"]
capital = [["New Delhi","Mumbai"], ["Beijing","vuhan"], ["Tokyo","kanto"], ["Washington DC","chikago"], ["London","wembly"], ["Moscow","amur"]]

dict1 ={}

# for (k,v) in zip(country,capital):
#     dict1[k] = v
     
#dict1 = {k:v for(k,v) in zip(country,capital)}
dict1 = {k:v for(k,v) in zip(country,capital)}
print(dict1)        