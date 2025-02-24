patternList = ["^", "()", "$", "%", "&", "*"]
pattern = ""

userInput = input('Enter the number of rows : ')

if userInput.isdigit() != True:
    print("Please enter a numeric value.")
    quit()

rows = int(userInput)

while(pattern not in patternList):
    pattern = input('Enter a pattern from these options [^, (), $, %, &, *] : ')

for i in range(rows + 1):
    for y in range(rows - i):
        print(" ", end = "")
    for a in range(i):
        print(pattern , end = "")
    print()

