vowels = set('aeiou')
word = input("Upisite rec: ")
found = vowels.intersection(set(word))
for vowels in found:
    print(vowels)