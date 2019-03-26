#Program 9 that reads in text file and output every second line

#Include sys and regular expression modules
import sys
import re
#Take command line argument and assign to string tit
tit = sys.argv[1]
#Remove "txt" text file extention
tit = tit.rstrip(".txt")
#Use regex to get rid of hyphen
tit = re.sub("-", " ", tit)
#Display file name as a title and make a capitalization of the first letter of each word in the title
print("Title:", tit.title())

#Open text file pointed in command line  
with open(sys.argv[1], "r") as txt:
    #Create loop to display every second line of text file starting and including first line
    for i, l in enumerate(txt, start=1):
        if i%2 == 0:
            print(l)



