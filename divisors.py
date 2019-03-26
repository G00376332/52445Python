#Program 3 that prints all numbers between 1000-10000 that are divisible by 6 but not 12

#Set the required range to check and step
for i in range(1000,10000,1): 
    #Check the condition if number is divisible by 6 but not 12 by using modulus operator
    if (i%6 == 0 and i%12 !=0): 
        #Print results if above condition is meet
        print(i) 
       

