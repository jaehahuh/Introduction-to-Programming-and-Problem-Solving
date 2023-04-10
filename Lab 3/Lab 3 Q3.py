first_leg = int(input("Please enter the first leg: "))
second_leg = int(input("Please enter the second leg: "))
hypo = float(input("Please enter the hypotenuse: "))

distance = first_leg**2 + second_leg**2 
if (abs(distance - (hypo**2) <= 0.00001)):
    print (first_leg,",",second_leg, "and", hypo, "form a right triangle.")
else:
    print (first_leg,",", second_leg, "and", hypo, "do not form a right triangle.")
