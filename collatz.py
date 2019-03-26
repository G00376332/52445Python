#Program 4 that ask the user to input any positive integer and outputs the successive values of the following calculation. 
#At each step calculate the next step calculate the next value by taking the current value and, if it is even, divide it by two, but if is odd, multiply it by three and add one.
#Have the program end if the current value is one.

#Wait for number from user and assign to x.
x = int(input("Please enter a positive integer: ")) 
#Display the first entered number
print(x, end=" ") 
#Use while condition until x is 1
while x > 1: 
    if (x%2 == 0): 
        x = x/2
        #Display number even number and do not add new line
        print(int(x), end=" ") 
    else:
        x = (x*3)+1
        #Display number odd number and do not add new line
        print(int(x), end=" ")
print()
