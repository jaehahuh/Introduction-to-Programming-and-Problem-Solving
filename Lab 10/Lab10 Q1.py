def write_name (filename, first_name, last_name):
    new_file = open (filename, "w")
    new_file.write(first_name)
    new_file.write(last_name)
    new_file.close()

def write_name(filename, first_name, last_name): # this one is better
    with open(filename, 'w') as f:
        f.write(first_name + ' ' + last_name)


def main():
    filename = input("What is a file name?: ")
    first_name = input("What is the first name?: ")
    last_name = input("What is the last name?: ")
    write_name(filename,first_name,last_name)

main()
   
