string = input("Enter an odd length string: ")

n = (len(string)//2)

print ("Middle character: ", string[n])
print ("First half: ", string[ :n])
print ("Second half: ", string [n+1: ])
