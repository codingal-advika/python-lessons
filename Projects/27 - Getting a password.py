import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# Specify password length
password_length = int(input('How many digits do you want your password to be? '))
random_password = generate_password(password_length)
if random_password:
    print("Generated Password:", random_password)







































# uc = ['A' , 'B' , 'C' , 'D' , 'E'  ,'F' , 'G' , 'H' , 'I'  , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' ,'Q' , 'R' , 'S' , 'T' , 
#     'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
# lc = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' ,'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' ,  
#     'u'  ,'v' , 'w' , 'x' , 'y' , 'z']
# num = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0]
# sym  = ['!' , '£' , '$', '%' , '^' , '&' , '*' ,'()']

# import random
# un = random.randint(0,25)
# n = random.randint(0,9)
# s =  random.choice(sym)
# pwd = uc[un] + lc[un] + num[n] + sym[s]
# print('Your random password is: ' , pwd)
# print('Click the play button at the top right corner to create a new password!')
