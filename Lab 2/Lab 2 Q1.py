import math

rad = int(input("Please enter an integer for radius: "))
circum_cir = 2*math.pi*rad
area_cir = math.pi*(rad**2)

print ("Circumference of the circle is:", round(circum_cir,2), "and the area of the circle is:", round(area_cir,2))
