s = input("Please enter string s: ")
k = int(input("Please enter a number k: "))
s1 = ""
s2 = ""
result = ""

while (s != ""):
    s1 = s[ :k] 
    s = s[k: ]
    s2 = s [ :k]
    s = s[k: ]
    result += s1[ : :-1]
    result += s2
    
print ("The output is: ", result)
