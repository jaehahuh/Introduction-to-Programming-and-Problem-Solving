leng_seq = int(input("Please enter the length of the sequence: "))

total_seq = 1
print("Please enter your sequence: ")
for i in range (1,leng_seq+1):
    seq = int(input())
    total_seq *= seq

geo_mean = total_seq**(1/leng_seq)

print ("The geometric mean is: ", round(geo_mean,4))
