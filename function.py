#Program 10 that displays a plot of the functions x, x^2 and 2^x in the range [0,4].
from numpy import arange
from matplotlib import pyplot as plt

x = arange(0,5)
cur1 = x
cur2 = pow(x,2)
cur3 = pow(2,x)

plt.plot(x,cur1 )
plt.plot(x,cur2 )
plt.plot(x,cur3 )
plt.xlabel('Range')
plt.ylabel("Funtions")
plt.legend()

plt.show()