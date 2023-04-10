side = int(input("Enter the number of sides: "))

if (side == 3):
    print ("The shape is triangle.")

elif (side == 4):
    q1 = input("Are the sides equal? (Y/N): ")
    if (q1 == "Y"):
        q2 = input("Are the angles 90 degrees? (Y/N):")
        if (q2 == "Y")
            print ("The shape is squares.")
        else:
            print ("The shape is rhombus.")
    else:
        q2 = input("Are the angles 90 degrees? (Y/N): ")
        if (q2 == "Y"):
            print ("The shape is rectangles.")
        else:
            print ("The shape is quadrilateral.")

else:
    print ("The shape is pentagons.")
