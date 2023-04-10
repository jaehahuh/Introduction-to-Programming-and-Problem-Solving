char = input("Enter a character: ")

if (char >= "A" and char <= "Z"):
    print (char, "is a upper case letter.")
elif (char >= "a" and char <= "z"):
    print (char, "is a lower case letter.")
elif (char >= "0" and char <= "9"):
    print (char, "is a digit.")
else:
    print (char, "is a non-alphanumeric character.")
