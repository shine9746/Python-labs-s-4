#Python programme to display following: 
import datetime

current = datetime.datetime.now()

print("Current date and time is : ",current)

print("Current year : ",current.strftime("%Y"))

print("Month of year : ",current.strftime("%B"))

print("Week number of the year : ",current.strftime("%W"))

print("Weekday of the week : ",current.strftime("%w"))

print("Day of year : ",current.strftime("%j"))

print("Day of the month : ",current.strftime("%d"))

print("Day of week : ",current.strftime("%A"))