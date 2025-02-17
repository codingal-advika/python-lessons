rows = int(input('Enter the number of rows : '))
print('!\n ') 
print('£\n')
print('$\n')
print('%\n')
print ('&\n')
print('*\n')
pattern = input('Enter a pattern from the options above : ')
for i in range(rows) :
    for col in range(i+1 ):
        print(pattern , end = '')
    print()
