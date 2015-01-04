import re
import datetime

dateripregex = "(\d\d?/\d{2}\t\d\d?:\d{2}\t\d\d?:\d\d)"

s = open('schedule.txt')
sfull = s.read()
s.close()
sstrip = re.findall(dateripregex, sfull) #this gives each line in a list, but still has tabs


#Subject, Start Date, Start Time, End Date, End Time, All Day Event, Description, Location, and Private.
#Work, $1, $2, $1, $3, N, , 1000 4th St SW"," Mason City"," 50401, False