word = input("Enter a word: ")

lower_case = word.lower()
vowel = "aeiou"

count_vowel = 0
count_consonant = 0

for char in lower_case:
    if char in vowel:
        count_vowel += 1
    else:
        count_consonant += 1

print (word, "has", count_vowel, "vowels and", count_consonant, "consonant.")
