import random
print ("I thought of a number between 1 and 100! Try to guess it. ")
print ()

n = random.randint(1,101)
guess = 0
min_num = 1
max_num = 100
count = 5
check = 0

while (guess != n and count != 0):
    print ("Range: [",min_num,",",max_num,"], Number of guesses left:", count)
    guess = int(input("Your guess: "))
    count -= 1
    check +=1
    if (count == 0):
        print ("Out of guesses! My number is", n)
    elif (guess < n):
        print("Wrong! my number is bigger")
        print ()
        min_num = guess + 1
    elif (guess > n):
        print ("Wrong! my number is smaller")
        print ()
        max_num = guess - 1
    else:
        print("Congrats! You guessed my number in", check, "guesses.")


