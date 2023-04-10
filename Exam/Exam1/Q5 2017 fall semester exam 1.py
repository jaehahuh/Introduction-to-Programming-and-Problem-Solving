print("How many numbers do you wish to enter?")
lines = int(input())
print ("Enter a sequence of", lines, "positive integers, each in a separate line:")
min_sum = 999999
line = 0
number = 0
sum_n = 0

while (lines>0):
    lines = lines - 1
    num = int(input())
    copynum = num
    line += 1
    sum_n = 0
    while (copynum > 0):
        sum_n += copynum % 10
        copynum = copynum // 10
    if( sum_n <= min_sum): # <= last value, < before value 
        min_sum = sum_n
        number = num
        final_line = line
print (number, "is a number with the smallest sum-digits. You entered it on line", final_line)
