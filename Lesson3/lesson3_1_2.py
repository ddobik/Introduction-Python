# Работает
# print(sum([int(num) for num in input('Enter three digit number: ')]))

# Работает
# a = [int(num) for num in input('Enter three digit number: ')]
# print(sum(a))

# Работает
# x = input('Enter three digit number: ')
# x = [int(num) for num in x]
# print(sum(x))

# Не работает!!! (Есть пробел в понимании)
x = input('Enter three digit number: ')
for num in x:
    x = [int(num)]
print(sum(x))
