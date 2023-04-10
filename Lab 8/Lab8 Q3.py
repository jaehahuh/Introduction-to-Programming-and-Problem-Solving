def encodeBinary (s):
    count = 1
    length = str()
    for i in range (1,len(s)):
        if (s[i-1] == s[i]):
            count += 1
        else:
            length +=  str(count) + " " + s[i-1] + "'s\n"
            count = 1

    length += str(count) + " " + s[i] + "'s"
    return length


def main ():
    s = input("Enter a number combined by 1s and 0s: ")
    print (encodeBinary(s))

main ()
