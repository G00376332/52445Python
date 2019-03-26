#Program 2 that checks if day begins with letter T

#Use datetime module
import datetime  
#Check if today's day is Tuesday or Thursday
if (datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3): 
  print("Yes - today begins with a T")
else:
  print("No - today does not begin with a T")