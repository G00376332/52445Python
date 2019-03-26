#Program 6 that takes entered text and outputs every second word

#Wait for text from user and assign to text
text = input("Please enter a sentence: ") 
#Create loop and split entered text by space
for idx, word in enumerate (text.split(" ")): 
        #Check and print every second word
        if idx % 2 == 0: 
                print (word,end=" ")

