def max_abs_val(lst):
    abs_lst = []
    max_num = 0
    for i in lst:
        abs_lst.append(abs(i))
    for num in abs_lst:
        if (num>max_num):
            max_num = num
        else:
            max_num = max_num
    return max_num
        







def main ():
    lst = [-19, -3, 20, -1, 0, -25]
    print (max_abs_val(lst))    

main()
