#Program 1 to calculate sum of all numbers between one and number entered by user

# Wait for number from user and assign to x
x = int(input("Please enter a positive integer:")) 
#Create variable "sum"
sum = 0 
#Check if entered number is a positive number
if x > 0:
    #Using "for" statement summarize all numbers in range based on number entered by user.
    for n in range (0,x+1,1): 
        sum = sum+n
    #Display result
    print("Sum of all numbers between 1 and", x, "is:", sum)
else:
    print("This is not a positive number!")