'''Identify the radius (r) of the circle.
Square the radius (r²).
Multiply the squared radius by π (approximately 3.14).
The result is the area of the circle'''
'''Steps:
Identify the radius of the circle. For example, let’s say the radius is 5 cm.
Multiply the radius by 2. 
2*5=10
Multiply the result by10 π (pi). 3.14159
≈
31.42'''
print('This code is to only try out the radius of whole numbers.')
class circle :
    def __init__(self , radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)
    def perimeter(self):
        return 2 * 3.14159 * self.radius
try:
    user_radius  =int(input('Enter the radius of your circle: '))
    circle = circle(user_radius)
    print(f'The Area of circle is {round(circle.area()  , 2)}')
    print(f'The Area of circle is {round(circle.perimeter()  , 2)}')
except ValueError:
    print('Please enter a whole number!')