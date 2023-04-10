import random

def main():
    n = int(input("Enter a positive integer: "))
    lst = []
    for i in range (1, n+1):
        lst.append(i)
    for i in range (3):
        shuffle_list(lst)
        print("#",i+1, end = ": ")
        for item in range(1, len(lst)):
            print (lst[item-1], end=", ")
        print (lst[item])

def shuffle_list(lst):
    for i in range (len(lst)):
        random_index = random.randint(0,len(lst))
        value = lst.pop(i)
        lst.insert(random_index, value)
    

main()
