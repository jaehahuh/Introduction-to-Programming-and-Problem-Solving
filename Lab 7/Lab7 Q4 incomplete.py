s = input("Please enter string s: ")
start = 0
end = 0
reverse_s = ""
for char in s:
    if (char == " "):
        reverse_s += s[start:end][ : :-1] + " "
        start = end + 1
    
reverse_s += s[start:end][ : :-1] + " "
print (reverse_s)
