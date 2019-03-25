#Program that display current data and time in format "Monday, January 10th 2019 at 1:15pm"

#Import date and time from datetime module
from datetime import datetime
#Take current date and time
now = datetime.today()
#display date and time using appropriete format string
print(now.strftime("%A, %B %d %Y at %I:%M%p"))


