#Python programme to get the days between 2 dates
from datetime import date

date1 = date(year=2000,month=2,day=28)
date2 = date(year=2001,month=2,day=28)

days = date2 - date1

print("Date 1 : ",date1)
print("Date 2 : ",date2)

print("The days in between the given dates are: ",days)