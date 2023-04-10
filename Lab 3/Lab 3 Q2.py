name = input("Please enter your name: ")
grad_year = int(input("Please enter your graduation year: "))
curr_year = int(input("Please enter current year: "))

diff_year = grad_year - curr_year

if (diff_year == 4):
    print (name, "is a Freshman.")
elif (diff_year == 3):
    print (name, "is a Sopomore.")
elif (diff_year == 2):
    print (name, "is a Junior.")
elif (diff_year ==1):
    print (name, "is a Senior")
else:
    print (name, "is Graduated")
