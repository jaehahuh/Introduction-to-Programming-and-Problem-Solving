s = input ("Please enter a string: ")

s2 = ""
for char in s:
    if (char.isupper()):
        s2 += char.lower()
    elif (char.islower()):
        s2 += char.upper()
    else:
        s2 += char

print ("New string is:", s2)
