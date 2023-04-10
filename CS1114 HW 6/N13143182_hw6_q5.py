def string_encoder(string):
    char_list = []
    encorded_list = []
    previous_char = string[0]
    count = 0
    for char in string:
        if char != previous_char:
            char_list = [previous_char, count]
            encorded_list.append(char_list)
            previous_char = char
            count = 1
        else:
            count += 1
    char_list = [previous_char, count]
    encorded_list.append(char_list)
    return encorded_list

    
def string_decoder(lst):
    decoded_string = ""
    for i in range (len(lst)):
        char = lst[i][0]
        count = lst[i][1]
        decoded_string += char * count
    return decoded_string






def main ():
    string = "aadccccaa"
    print (string_encoder(string))
    
    lst = [['a',2], ['d',1], ['c',4], ['a',2]]
    print (string_decoder(lst))

main()
