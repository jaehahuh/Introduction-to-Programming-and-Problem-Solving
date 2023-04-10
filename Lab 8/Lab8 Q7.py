def find (some_string, substring, start, end):
    for i in range (start, end):
        sub = some_string [i : i + len(substring)]
        if substring == sub :
            return i
    return -1
    
print(find("hellohellohello", "he", 0, 11))
        

def multi_find (some_string, substring, start, end):
    lst = []
    index = find(some_string, substring, start, end)
    while index != -1:
        lst.append(index)
        index = find(some_string, substring, index + 1, end)
    return lst

print(multi_find("hellohellohello", "he", 0, 11))
