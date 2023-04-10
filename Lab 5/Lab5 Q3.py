first_n = input("Please enter the first number: ")
second_n = input("Please enter the second number: ")

count = 0
if (len(first_n) == len(second_n)):
    num1 = int(first_n)
    num2 = int(second_n)
    
    for i in range (len(first_n)):
        num1_r = num1%10
        num2_r = num2%10
        num1 = num1//10
        num2 =  num2//10
        
        if(num1_r == num2_r):
            count += 0
        else:
            count += 1

else:
    print("Those number have different digits")

print("The Hamming Distance between", first_n, "and", second_n, "is", count)
