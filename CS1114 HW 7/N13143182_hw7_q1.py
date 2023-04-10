import random

def pick_a_random_word(inFile):
    with open(inFile) as file:
          file_words = file.read()
    words = file_words.split()
    line = random.randint(0, len(words))
    return words[line]
        
def create_permutation(n):
    num_lst = []
    for i in range (n):
        num_lst.append(i)
    random.shuffle(num_lst)
    return num_lst

def scramble_word(word):
    n = len(word)
    scrambled_word = ""
    for i in create_permutation (n):
        scrambled_word += word[i] + " "
    return scrambled_word

def main ():
    word = pick_a_random_word("hw7 - word bank.txt")
    scrambled_random_word = scramble_word(word)
    print("Unscramble the word:" + scrambled_random_word)
    for num in [1,2,3]:
        try_num = input("Try #" + str(num) +": ")
        if (try_num == word):
            print ("Yay you got it")
            break
        else:
            print ("Wrong!")


main()
