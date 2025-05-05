'''Write a program to overload the less than (<) and equal to (==) operators.
For example, create objects - ob1 and ob2 with values 3 and 4
to compare values, respectively. You can additionally create more objects to try different values.'''

class lessthan:
    def __init__ (self  , a):
        self.a = a

    def __lt__ (self , other):
        self.other = other
        if self.a < other.a:
            return 'Ob1 is less than OB2'
        else:
            return 'OB1 is greater than OB2'
    def __equal__(self , other):
        if self.a == other.a:
            return 'OB1 is equal to OB2'
        else:
            return 'OB1 is not equal to OB2'
ob1 = (2)
ob2 = (3)
print(f'{ob1} is lesser than {ob2} ')
print(f'{ob1} and {ob2} are not equal to eachother')



    

    
