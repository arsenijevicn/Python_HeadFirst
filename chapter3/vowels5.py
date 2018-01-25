vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Input word: ")
found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k in sorted(found):
    print(k, 'was found', found[k], 'time(s).')
