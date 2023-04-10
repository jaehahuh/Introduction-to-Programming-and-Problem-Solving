print("Please enter a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing done: ")

leng_seq = 0
total_seq = 1

done = False

while (not done):
    seq = input()
    if (seq == "done"):
        done = True
    else:
        seq = int(seq)
        total_seq *= seq
        leng_seq +=1

geo_mean = (total_seq**(1/leng_seq))

print ("The geometric mean is: ", round(geo_mean,4))
        
