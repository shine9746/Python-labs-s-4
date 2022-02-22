#Python programme to display following: 
import datetime

current = datetime.datetime.now()

print("Current date and time is : ",current)

print("Current year : ",current.strftime("%Y"))

print("Month of year : ",current.strftime("%B"))

print("Week number of the year : ",current.strftime("%U"))

print("Weekday of the week : ",current.strftime("%A"))

print("Day of year : ",current.strftime("%j"))

print("Day of the month : ",current.strftime("%d"))

print("Day of week : ",current.strftime("%w"))
