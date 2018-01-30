vowels = {'a', 'o', 'e', 'o', 'i', 'e', 'o', 'u', 'i', }
print(vowels)

vowels2 = set('aeeiiouuu')
print(vowels2)

vowels3 = set('aeiou')
word = 'hello'

u = vowels3.union(set(word))
print(u)
u_list = sorted(list(u))
print(u_list)
