#Program that takes entered text and outputs every second word.

text = input('Please enter a sentence: ') #Wait for text from user and assign to text.

for idx, word in enumerate (text.split(' ')): #Create loop and split entered text by space
    if idx % 2 == 0: #Check and print every second word
        print (word,end=' ')

