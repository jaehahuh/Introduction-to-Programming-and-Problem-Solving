password = input("Enter a password: ")

length_password = len(password)
count_upper = 0
count_lower = 0
count_digit = 0
count_special = 0
special_char = "!@#$"

for char in password:
    if (char.isupper()):
        count_upper += 1
    elif (char.islower()):
        count_lower += 1
    elif (char.isdigit()):
        count_digit += 1
    elif (0 <= special_char.find(char)):
        count_special += 1

if (length_password < 8):
    print (password, "is not a valid password.")
elif (count_upper < 2):
    print (password, "is not a valid password.")
elif (count_lower < 1):
    print (password, "is not a valid password.")
elif (count_digit < 2):
    print (password, "is not a valid password.")
elif (count_special < 1):
    print (password, "is not a valid password.")
else:
    print (password, "is a valid password.")
