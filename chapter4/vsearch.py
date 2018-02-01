def search4vowels():
    """Displays any vowels found in asked-for word"""
    vowels = set('aeiou')
    word = input("Upisite rec: ")
    found = vowels.intersection(set(word))
    for vowels in found:
        print(vowels)


search4vowels()
