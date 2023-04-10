def create_prefix_lists(lst):
    item_list= []
    collected_list = [[]]
    for i in lst:
        item_list.append(i)
        prefix_list = []
        prefix_list.extend(item_list)
        collected_list.append(prefix_list)
    return collected_list
        







def main():
    lst = [2, 4, 6, 8, 10]
    print (create_prefix_lists(lst))


main()
    
