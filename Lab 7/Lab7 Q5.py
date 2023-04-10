s = input("Please enter a string s: ")
sub_s = ""
for i in range (1,len(s)//2+1):
    if (len(s)%i == 0):
        sub_s = s[0:i]
        count = int(len(s)/i)
if (sub_s*count == s):
    print ("The substring",  sub_s, "repeated", count, "times in ", s)
else:
    print ("There are no repeating substrings in", s)
