def reverse_to_new_list(lst1):
    rev_lst1 = []
    for i in lst1:
        rev_lst1.insert(0,i)
    return rev_lst1
        

def reverse_in_place(lst2):
    for i in range (len(lst2)//2):
         temp_index = lst2[i]
         lst2[i] = lst2[len(lst2) - i -1]
         lst2[len(lst2) - i -1] = temp_index
    return lst2 
        







def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1, "and the returned list is", rev_lst1)

    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place (lst2)
    print("After reverse_in_place, lst2 is", lst2) 


main()
