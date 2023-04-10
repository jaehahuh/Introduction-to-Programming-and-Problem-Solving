a = input ("Please enter string a: ")
b = input ("Please enter string b: ")

a_len = len(a)
b_len = len(b)

if (a_len > b_len):
    print ("The output is: ", b + a + b)
else:
    print ("The output is: ", a + b + a)

