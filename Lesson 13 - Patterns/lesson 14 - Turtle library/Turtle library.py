import turtle
n = int(input('Enter the number of sides : '))
lenght = int(input('Enter sides length : '))
a  = 360 / n
turtle.Screen().bgcolor('purple')
turtle.Screen().setup(556,356)
pen = turtle.Turtle()
for i in range(n) :
    pen.forward(lenght)
    pen.right(a)
turtle.done()



