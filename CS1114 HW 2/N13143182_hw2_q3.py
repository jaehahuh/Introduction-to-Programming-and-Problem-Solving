import math
import turtle

a = int(input("Please enter a first segment: "))
b = int(input("Please enter a second segment: "))
angle_c = int(input("Please enter a angle between segments:" ))

c = math.sqrt((a**2) + (b**2) - 2*a*b*math.cos(math.radians(angle_c)))
angle_a = math.degrees(math.acos(((b**2)+(c**2)-(a**2))/(2*b*c)))

turtle.forward(a)
turtle.left(180-angle_c)
turtle.forward(b)
turtle.left(180-angle_a)
turtle.forward(c)



