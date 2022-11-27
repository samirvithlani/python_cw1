from datetime import date

#myDate = date.today()
myDate = date(1)
#print(myDate)
minDate = date.min
print(minDate)
maxDate = date.max
print(maxDate)


#1970-01-01

today = date.today(1)
print(today)
print("year: ",today.year)
print("month: ",today.month)
print("day: ",today.day)
print("weekday",today.weekday())
print("iso weekday",today.isoweekday())
print(today.isoformat())





#print(myDate)