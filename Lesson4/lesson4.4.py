n = int(input('Enter n<=9:'))
l: list = list(range(1, n + 1))
for item in l:
    s: list = list(range(1, item+1))
    p = ''.join(str(x) for x in s)
    print(p)
