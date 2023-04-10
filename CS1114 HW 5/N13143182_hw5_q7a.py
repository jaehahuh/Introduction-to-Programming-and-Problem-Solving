print ("Enter number in the simplified Roman system:")
roman = input ()
number = 0

if (roman.count("D") > 1):
    number = "not legal number."
elif (roman.count ("L") > 1):
    number = "not legal number."
elif (roman.count ("V") > 1):
    number = "not legal number."
elif (roman.count ("C") > 4):
    number = "not legal number."
elif (roman.count ("X") > 4):
    number = "not legal number."
elif (roman.count ("I") > 4):
    number = "not legal number."
else:
    for char in roman: 
        if (char == "I"):          
            number += 1
        elif (char == "V"):
            number += 5
        elif (char == "X"):
            number += 10
        elif (char == "L"):
            number += 50    
        elif (char == "C"):
            number += 100   
        elif (char == "D"):
            number += 500
        elif (char == "M"):
            number += 1000

print (roman, "is", number)
