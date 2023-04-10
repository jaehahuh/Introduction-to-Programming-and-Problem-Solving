expression = input("Enter a mathmatical expression: ")

n = expression.find(" ")

operand1 = expression [ :n]
operator = expression [n+1]
operand2 = expression [n+3 : ]

operand1 = int(operand1)
operand2 = int(operand2)

if (operator == "+"):
    value = operand1 + operand2
elif (operator == "-"):
    value = operand1 - operand2
elif (operator == "*"):
    value = operand1 * operand2
elif (operator == "/"):
    value = operand1 / operand2

print  (expression, "=", value)
