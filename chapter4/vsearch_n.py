# komentar: ovo su anotacije(opisi), ali su zbunjujuci
def search4vowels(phrase: str) -> set:
    """Returns any vowels found in suplied word"""
    vowels = set("aeiou")
    return print(vowels.intersection(set(phrase)))


# search4vowels("hitch-hiker")
# search4vowels replaced with search4letters, 2nd parameter is optional

def search4letters(phrase: str, letters: str = "aeiou") -> set:
    """Returns set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


help(search4letters)
print(search4letters("hitch-hiker"))
print(search4letters("life, universe and everything", "o"))
print(search4letters("galaxy", "xyz"))
print(search4letters(letters="xyz", phrase='galaxy'))
