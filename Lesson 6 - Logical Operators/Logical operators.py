a = int(input('Enter number'))
b = int(input('Enter number'))
if a > b and b > 0 and a > 0 :
    print('A is greater than B ,and both the numbers are positive')
else :
    print('B is greater than  A, or any one of the numbers are negetive')
# Or operators

x = int(input('Enter your number'))
y = int(input('Enter your number'))
if x < y or y > 1 or x > 0 :
    print('True')
else :
    print('False')

# Not operators

m= input('Enter a word')
n= input('Enter a word')
if m != n:
    print('m and n hold different values')
else :
    print('m and n hold the same values')