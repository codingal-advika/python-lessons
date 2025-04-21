# 1. create class IOstring
# 2. create constructor
# __init__

# 3. self.str1 = ' '

# 4. create a method uinput

# self.str1 = input('Enter the string')

# 5. create another method poutput

# print( ' the string in uppercase', self.str1.uppercase()

# 6. create an object

# 7. call all the 2 methods

class IOstring:
    def __init__(self):
        self.str1 = ''
    def uinput(self):
        self.str1 = input('Enter a string: ')
    def poutput(self):
        print('The string in uppercase is :' ,self.str1.upper() )
ob = IOstring()
ob.uinput()
ob.poutput()


