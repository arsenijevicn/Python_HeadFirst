fruits = {}
fruits['apples'] = 10
print('apples' in fruits)

if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

print(fruits)

fruits.setdefault('pears', 0)
fruits['pears'] += 1

print(fruits)