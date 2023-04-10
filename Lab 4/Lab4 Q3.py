a = int(input("Please enter a positive integer as the dividend: "))
b = int(input("Please enter a positive integer as the divisor: "))

c = a
count = 0
while (c>b):
    c -= b
    count += 1
    

print ("Quotient of", a, "divided by", b,"is: ", count)
