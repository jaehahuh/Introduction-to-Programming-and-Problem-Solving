print ("Enter decimal number: ")
decimal_num= input()

num = (1000, 500, 100, 50, 10, 5, 1)
roman = ("MDCLXVI")
result = ""
number = int(decimal_num)

for i in range(len(num)):
    count = int(number / num[i])
    number -= num[i] * count
    result += roman[i] * count    

print(decimal_num, "is", result)

