#Python programme to convert unix timestamp string to readable date

import time
from datetime import datetime

unixTimestamp  = int(time.time())                #current unix timestamp
tostring = str(unixTimestamp)                    #as string

print("Current unix timestamp string : ","\'",tostring,"\'")


unixtimestamp = int(tostring)                    #back to int
date = datetime.fromtimestamp(unixtimestamp)      

convertedDate = date.strftime("%d-%m-%Y")
print("Unix timestamp to date :", convertedDate)	



