uc = ['A' , 'B' , 'C' , 'D' , 'E'  ,'F' , 'G' , 'H' , 'I'  , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' ,'Q' , 'R' , 'S' , 'T' , 
    'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
lc = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' ,'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' ,  
    'u'  ,'v' , 'w' , 'x' , 'y' , 'z']
num = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0]
sym  = ['!' , '£' , '$', '%' , '^' , '&' , '*' ,'()']

import random
un = random.randint(0,25)
n = random.randint(0,9)
s =  random.choice(sym)
pwd = uc[un] + lc[un] + num[n] + sym[s]
print('Your random password is: ' , pwd)
print('Click the play button at the top right corner to create a new password!')

