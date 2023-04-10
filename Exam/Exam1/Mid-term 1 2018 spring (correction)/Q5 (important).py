n = int(input("What is your number: "))
for digit in range (10):
    count = 0
    val = n
    while (val > 0):
        if (val%10 == digit):
            count += 1
        val//=10
    if (count>0):
        print (digit,"appears",count,"time(s)")
