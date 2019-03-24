#Program that ask the user to input any positive integer and outputs the successive values of the following calculation. 
#At each step calculate the next step calculate the next value by taking the current value and, if it is even, divide it by two, but if is odd, multiply it by three and add one.
#Have the program end if the current value is one.

x = int(input('Please enter a positive integer: ')) #Wait for number from user and assign to x.

print(x, end=' ') #Display the first entered number

while x > 1: #Using while repeat operation until x is 1
    
    if (x%2 == 0): #Check if number is even using moduluds operator and if is true devide by 2  
        x = x/2
        print(int(x), end=' ') #Display integer number and do not add new line
    else:
        x = (x*3)+1
        print(int(x), end=' ')
print()
