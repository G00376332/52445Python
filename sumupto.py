#Program to calculate sum of all numbers between one and number entered by user

x = int(input('Please enter a positive integer:\n')) # Wait for number from user and assign to x.

sum = 0 #Create variable sum

for n in range (0,x+1,1): #Using "for" statement sumarize all numbers in range based on number entered by user.
    sum = sum+n

print('Sum of all numbers between 1 and', x, 'is:', sum)