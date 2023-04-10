string = input("Please enter a string of lowercase letters: ")

for i in range (len(string)-1):
    if (string[i] <= string[i+1]):
        if (i == len(string)-2):
            print (string, "is increasing.")
    else:
        print (string, "is not increasing")
        break
