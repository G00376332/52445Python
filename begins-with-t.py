#Program that checks if day begins with letter T

import datetime #Assign curent date and time 
print(datetime.datetime.today().weekday())

if (datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3): # Check if todays day is Tuesday or Thursday
  print("Yes - today begins with a T")
else:
  print("No - today does not begin with a T")