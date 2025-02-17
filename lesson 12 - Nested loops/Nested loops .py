word = input('Enter a word ')
char = input('Enter a character from the word ')
index = 0
count = 0
while index < len(word) :
    if word [index]== char :
        count = count + 1 
    index = index + 1
print ('The ', char , ' has occured ' , count ,' times' )
