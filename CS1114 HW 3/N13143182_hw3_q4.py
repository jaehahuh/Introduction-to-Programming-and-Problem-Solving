import math

a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))

if (a == 0 and b == 0 and c == 0):
    print ("This equation has infinite number of solutions")
elif (a == 0 and b == 0 and c != 0):
    print ("This equation has no solution.")
else:
    discriminant = ((b**2) - 4*a*c)
    x1 = (-b + math.sqrt((b**2) - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt((b**2) - 4*a*c))/(2*a)

    if (discriminant > 0):
        print ("This equation has double real solutions x =", x1, "and x =", x2)
    elif (discriminant == 0):
        print ("This equation has single real solution x=", x1)
    else:
        print ("this equation has no real solution.")
