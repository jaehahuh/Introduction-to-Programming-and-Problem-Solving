a = int(input("Please enter a positive integer as the dividend: "))
b = int(input("Please enter a positive integer as the divisor: "))

c=a

while (c>b):
    c -= b

print ("Remainder of", a, "divided by", b,"is: ", c)
