char = input("Enter a character: ")

if (char.isupper()):
    print (char, "is a upper case letter.")
elif (char.islower()):
    print (char, "is a lower case letter.")
elif (char.isdigit()):
    print (char, "is a digit.")
elif (not char.isalpha()):
    print (char, "is a non-alphanumeric character.")
