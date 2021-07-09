x = int(input('Enter x:'))
f = 1
for i in range(2, x+1):
    f *= i
print(x, '!', '=', f)
