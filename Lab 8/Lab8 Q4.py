def consecutive_int (myint, n):
    lst = []
    for i in range (n):
        lst.append(myint)
        myint += 1
    return lst


def main ():
    myint = int(input("Enter a positive integer: "))
    n = int(input("Enter a positivie integer: "))
    print (consecutive_int (myint,n))

main()
