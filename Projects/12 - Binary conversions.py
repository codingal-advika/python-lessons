num = int(input('Enter a value3 : '))
binary = "" 
if num == 0 :
    print('0')
while num > 0 :
    remainder = num % 2
    num = num // 2
    binary = str(remainder) + binary
print('Your binary number is ' , binary)