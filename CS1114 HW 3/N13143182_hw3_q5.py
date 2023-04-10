print ("Please enter length of a triangle's sides.")
first = float(input("Length of the first side: "))
second = float(input("Length of the second side: "))
third= float(input("Length of the third side: "))

if (first== second and second == third):
    print(first, ',', second, ',', third, "form an equilateral triangle.")
elif (first == second != third or first != second == third or first != third == second):
    if (abs(first**2 - (second**2 + third**2)) <= 0.00001 or abs(second**2 - (first**2 + third**2)) <= 0.00001 or abs(third**2 - (first**2 + second**2)) <= 0.00001):
        print(first, ',', second, ',', third, "form an isosceles right triangle")
    else:
        print(first, ',', second, ',', third, "form an isosceles that is not a right triangle.")
else:
    print(first, ',', second, ',', third, "form a triangle that is not an isosceles and not an equilateral.")	
