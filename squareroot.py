#Program that calculate approximation of square root of entered number.

x = float(input('Please enter a positive number: ')) #Wait for number from user and assign to x.

#Check if entered number is a positive number
if x > 0:
    x_sqrt = x ** 0.5 #Calculate square root of entered number
    print('The square root of %0.1f is %0.1f' %(x ,x_sqrt)) #Display approximation up to 1 decimal place using %0.1f in print 
else:
    print(x, "is not a positive number") #Display a message that entered number is not a positive number
