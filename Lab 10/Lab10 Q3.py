def sum_column(filename):
    sum_num = 0
    with open (filename, "r") as new_file:
        for line in new_file.readlines():
            sum_num += int(line)
    return sum_num

def main():
    filename = input("Enter a file name: ")
    print(sum_column(filename))

main()
