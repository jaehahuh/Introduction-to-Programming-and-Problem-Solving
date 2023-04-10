import random

print("I thought of a number between 1 and 100!")
n = random.randint(1,101)

guess = 0
while (n != guess):
    guess = int(input("Try to guess what it is:"))
    if (guess>n):
        print("Wrong guess. My number is smaller than yours.")
    elif (guess < n):
        print ("Wrong guess. My number is bigger than yours.")

print ("Congrats! You guessed my number.")
    
    
    
