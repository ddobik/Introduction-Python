x = int(input('Enter three digit number: '))
digit_3 = x % 10
x = x // 10
digit_2 = x % 10
x = x // 10
print('Sum of digits of a number :', x + digit_2 + digit_3)
