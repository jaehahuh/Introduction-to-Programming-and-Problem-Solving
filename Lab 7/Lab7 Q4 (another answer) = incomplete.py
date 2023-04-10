s = input("Please enter string s: ")
result = ""
word = ""

for char in s:
    if char == " ":
        result += word[ : :-1] + " "
        word = ""
    else:
        word = char

result += word [ : :-1]

print(result) 
