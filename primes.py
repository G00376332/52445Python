#Program that check if entered number is a prime.

x = int(input('Please enter a positive integer: ')) #Wait for number from user and assign to x.

if x > 1: #Check if entered number is grater than 1

    for n in range(2,x): #Create loop to check if entered number is devidable by any other number than 1 and itself
        if(x % n) == 0:
            print("This is not a prime number")
            break
    else:
        print("That is a prime number")
    
else:
    print("This is not a prime number")
        
    
