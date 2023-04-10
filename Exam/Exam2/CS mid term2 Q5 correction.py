def find_uncommon (list1, list2):
    common = []
    for i in list1:
        if i not in list2:
            common.append (i)
    for i in list2:
        if i not in list1:
            common.append (i)
    return common




def print_nicely(lst):
    for i in lst:
        print (i + " ")
