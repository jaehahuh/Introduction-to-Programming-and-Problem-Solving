s = input("Please enter string s: ")
k = int(input("Please enter a number k: "))
result = ""

for i in range (0,len(s), 2*k):
    reverse = s[i : i +k][ : :-1]                                    
    keep = s[i+k : i+(2*k)]
    result += reverse + keep
    
print ("The output is: ", result)   
