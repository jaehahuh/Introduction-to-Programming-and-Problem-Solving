def func (string):
    current = string [0]
    count = 1
    for i in range (1,len(string)):
        if (current != string[i]):
            print (current, " ", count,"time's")
            current = string[i]
            count = 1
        else:
            count +=1
    print (current, " ",count, "times")


def main ():
    string = input()
    func(string)

main ()
