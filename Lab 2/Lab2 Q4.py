number = int(input("Please enter an integer less than 100: "))

countL = number//50
r_50 = number%50

countX = r_50//10
r_10 = r_50%10

countV = r_10//5
r_5 = r_10%5

countI = r_5//1

sum_roman = "L"*countL + "X"*countX + "V"*countV + "I"*countI

print(number, "in Roman Numeral is:", sum_roman)
