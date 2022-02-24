# Python program to get week number from 16/06/2015
from datetime import date

week  = date(year = 2015,month = 6,day=16)

weeknumber = week.strftime("%W")

print("The week number is : ",weeknumber)