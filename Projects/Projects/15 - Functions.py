def calculate_circumference (radius) :
    pi = 3.14
    circumference = radius * 2 * pi
    return circumference

userRadius = int(input('Enter the radius: '))
if userRadius < 0 :
    print('Enter a value greater than 0.')
else :
    circum = calculate_circumference(userRadius)
    print('The circumference of your cicle is equal to ' , circum)


