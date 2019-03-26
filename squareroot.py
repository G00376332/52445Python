#Program 7 that calculate approximation of square root of entered number

#Wait for number from user and assign to x
x = float(input("Please enter a positive number: ")) 

#Check if entered number is a positive number
if x > 0:
    #Calculate square root of entered number
    x_sqrt = x ** 0.5 
    #Display approximation up to 1 decimal place using %0.1f in print 
    print("The square root of %0.1f is approx. %0.1f" %(x ,x_sqrt)) 
else:
    #Display a message that entered number is not a positive number
    print(x, "is not a positive number") 
