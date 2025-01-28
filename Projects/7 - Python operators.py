userInput = input('Enter a character: ')
length = len(userInput)

if length != 1 :
    print('Please type in only one character')
else :
    asciiValue = ord(userInput)
    print(asciiValue)


