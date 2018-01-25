book = "the hitchhiker's guide to the galaxy"
book_list = list(book)
print(book_list)

print(book_list[0:3])
print(''.join(book_list[0:3]))
print(''.join(book_list[-6:]))

backwards = book_list[::-1]
print(''.join(backwards))

every_other = book_list[::2]
print(''.join(every_other))

print(''.join(book_list[4:14]))
print(''.join(book_list[13:3:-1]))