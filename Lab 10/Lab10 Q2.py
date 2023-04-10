import random

def write_random_numbers(filename, n):
    with open (filename, "w") as new_file:
        for line in range (n):
            new_file.write(str(random.randint(1,100))+ "\n")



def main():
    filename = input("Enter a file name: ")
    n = int(input("Enter a positive integer: "))
    write_random_numbers(filename,n)

main()
