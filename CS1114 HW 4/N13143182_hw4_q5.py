n = int(input("Please enter a positive integer: "))

for i in range (1, n):
    if (i%2 == 0 and i//10%2 == 0):
        print(i)
