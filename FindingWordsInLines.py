import string 

words = []
lines = []
output = []
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
text = open("document.txt", "r") 
textWords = open("document.txt", "r") 

#reads lines from the file
for line in text:
    line = line.lower()  #replaces uppercase letters with lowercase letters
    line = line.translate(line.maketrans("", "", string.punctuation)) #erases punctuation
    line = line.replace("\n"," \n") #adds space at the end of the line
    lines.append(" " +line) #stores space at the beginning and line as one element of the list
    
#reads words from the file
for word in textWords.read().split():
    word = word.lower() #replaces uppercase letters with lowercase letters
    word = word.translate(word.maketrans("", "", string.punctuation)) #erases punctuation
    words.append(word) #stores word int the list

words.sort() #sorting words alphabetically
words = list(dict.fromkeys(words)) 

#finds the word in the line and prints the number of the line
for word in words:
     print(word,":", end = " ")
     counter = 1
     for line in lines:
        found = line.find(" " + word + " ") #spaces are added to find exact word,and not substrings that appear in the file
        if found != -1:
            print(counter, end = " ")
        counter = counter + 1
     print(' ')
     

     
    
         
             