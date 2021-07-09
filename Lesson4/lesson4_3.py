a = int(input('Enter a:'))
b = int(input('Enter b:'))
if a < b:
    l: list = list(range(a, b + 1))
    str1 = ''.join(str(n) for n in l)
    print(str1)
elif a > b:
    l: list = list(reversed(range(b, a+1)))
    str1 = ''.join(str(n) for n in l)
    print(str1)
else:
    print(None)
