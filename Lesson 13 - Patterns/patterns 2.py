rows = int(input('Enter the number of rows : '))
n =1
for i in range( 1 , rows + 1) :
    for col in range(1 , i+1):
        print(n , end = ' ')
        n = n + 1
    print()