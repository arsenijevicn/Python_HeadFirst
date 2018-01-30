vowels = {'a', 'o', 'e', 'o', 'i', 'e', 'o', 'u', 'i', }
print(vowels)

vowels2 = set('aeeiiouuu')
print(vowels2)

vowels3 = set('aeiou')
word = 'hello'

u = vowels3.union(set(word))
print('Union is: {} '.format(u))

u_list = sorted(list(u))
print('Union (sorted) is: {} '.format(u_list))

d = vowels3.difference(set(word))
print('Difference is: {} '.format(d))

i = vowels3.intersection(set(word))
print('Intersection is: {} '.format(i))
