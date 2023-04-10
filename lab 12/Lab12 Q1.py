class Phonebook:
    def __init__:

def main():
    phonebook = {}
    inFile = open("Lab12-phonebook.txt", 'r')
    for line in inFile:
        line = line.strip()
        parts = line.split(",")
        last_name = parts[0]
        comb_first_num = parts[1]
        comb_parts = comb_first_num.split(" ")
        first_name = comb_parts[1]
        phone_number = comb_parts[2]
        name = first_name + ' ' + last_name

        add_entry (phonebook, name, phone_number)  
        
        
    return phonebook

def is_valid_phone_number (phone_number):
    return phone_number.isdigit() and len(phone_number) == 10
    
def add_entry (phonebook, name, phone_number):
    if name not in phonebook:
        if is_valid_phone_number(phone_number):
            phonebook[name] = phone_number
        else:
            print(phone_number, "is not a valid phone number")
    else:
        print(name, "is already exist in the phone book.")


def lookup (phonebook, name):
    if name in phonebook:
        print (phonebook[name])
    else:
        print (name, " 's phone number is not an recorded in the phone book.")


def print_all(phonebook):
    if name in phonebook:
        print(name, phonebook[name], sep=': ')






main()
