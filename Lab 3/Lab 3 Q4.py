a = int(input("Please enter a: "))
b = int(input("Please enter b: "))

if (a == 0 and b != 0):
    print("The equation has no solution.")
elif (a == 0 and b == 0):
    print("The equation has infinite number of solution.")
else:
    x = -b/a
    print("The equation has single solution and x = ", x)
