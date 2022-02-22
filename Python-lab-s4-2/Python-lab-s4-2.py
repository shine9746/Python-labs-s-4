#Python programme to subtract 5 days from the current date and display
from datetime import datetime,timedelta

currentdate = datetime.now() 

datedifference = timedelta(5)

print("Current date is : ",currentdate)

print("Five days before  the current date is : ",currentdate-datedifference)

