def search4vowels(phrase: str) -> set:  # komentar: ovo su anotacije(opisi), ali su zbunjujuci
    """Returns any vowels found in suplied word"""
    vowels = set("aeiou")
    return print(vowels.intersection(set(phrase)))


search4vowels("sky")
help(search4vowels)

