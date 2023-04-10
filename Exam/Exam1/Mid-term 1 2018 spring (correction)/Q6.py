total = 0
n = int(input("Please enter a positive integer:"))
for i in range (0,n+1):
    total += ((-1)**i) / ((2*i) +1)
print ("pi=", (4*total))
