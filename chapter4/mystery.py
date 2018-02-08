def double(arg):
    print("Before: ", arg)
    arg = arg * 2
    print("After: ", arg)


def change(arg):
    print("Before: ", arg)
    arg.append("More data")
    print("After: ", arg)


print("TOM:")

num = 10
print(double(num))
print(num)
print("******************")

saying = "Hallo "
print(double(saying))
print(saying)
print("******************")

numbers = [42, 256, 16]
print(double(numbers))
print(numbers)
print("******************")

print("SARA: ")
numbers1 = [42, 256, 16]
print(change(numbers1))
print(numbers1)
