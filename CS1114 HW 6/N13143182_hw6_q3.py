def add_list(lst1, lst2):
    add_lst = []
    for i in range (len(lst1)):
        add_lst.append(lst1[i]+lst2[i])
    return add_lst


def main():
    lst1 = []
    while True:
        num1 = input("Enter a list1 of numbers and enter 'done' ")
        if(num1 == "done"):
            break
        lst1.append(int(num1))
    
    lst2 = []
    while True:
        num2 = input("Enter a list2 of numbers and enter 'done' ")
        if(num2 == "done"):
            break
        lst2.append(int(num2))

    if (len(lst1) == len(lst2)):
        print(add_list(lst1, lst2))
    else:
        print("Lists are different lengths.")

        
main()
