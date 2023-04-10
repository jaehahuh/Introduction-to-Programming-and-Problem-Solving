def consecutive_char(ch, n):
    num_ch = ord(ch)
    string = str()
    for i in range (1,n+1):
        string += chr(num_ch)
        num_ch += 1
        if (num_ch > ord("z")):
            num_ch = ord("a")
    return string
    


def main ():
    ch = input ("Enter a character: ")
    n = int(input("Enter a positive integer: "))
    string = consecutive_char (ch,n)
    print (string)


main ()
