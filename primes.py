#Program 5 that check if entered number is a prime

#Wait for number from user and assign to x
x = int(input("Please enter a positive integer: ")) 
#Check if entered number is greater than 1
if x > 1: 
    #Create loop to check if entered number is divisible by any other number than 1
    for n in range(2,x): 
        if(x % n) == 0:
            print("This is not a prime number")
            break
    else:
        print("That is a prime number")
    
else:
    print("This is not a prime number")
        
    
