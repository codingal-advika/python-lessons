import math
angle = (input("Enter the angle in degrees: "))
if angle.isdigit() != True:
    print("Please enter a numeric value.")
angle2 = int(angle)
print("Sine:", math.sin(math.radians(angle2)))
print("Cosine:", math.cos(math.radians(angle2)))
print("Tangent:", math.tan(math.radians(angle2)))