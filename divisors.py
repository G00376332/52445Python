#Program that prints all numbers between 1000-10000 that are divisible by 6 but not 12

for i in range(1000,10000,1): #Set the required range to check and step
    if (i%6 == 0 and i%12 !=0): #Check the condition if number is divisible by 6 but not 12 by using modulus operator
        print(i) #Print results if above condition is meet

