def find_all(lst, val):
    val_list = []
    for i in range(len(lst)):
        if (lst[i] == val):
            val_list.append(i)
    return val_list







def main ():
    lst = ['a', 'b', '10', 'bab', 'a']
    val = 'a'
    print(find_all(lst, val))
            
main()

            
        
