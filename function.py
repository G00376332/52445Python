#Program 10 that displays a plot of the functions x, x^2 and 2^x in the range [0,4]

#Importing modules that are necessary for this task
from numpy import arange
from matplotlib import pyplot as plt

#Assign range for x 
x = arange(0,5)
#Create curves for display appropriate function
cur1 = x
cur2 = pow(x,2)
cur3 = pow(2,x)

#Plot curves
plt.plot(x,cur1 )
plt.plot(x,cur2 )
plt.plot(x,cur3 )
#Create axis labels
plt.xlabel('Range')
plt.ylabel("Funtions")
#Create legend with functions description
plt.legend(["x","x^2","2^x"])
#Display a chart
plt.show()