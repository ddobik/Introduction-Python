x = int(input('Enter year number: '))
if x % 4 != 0 or x % 100 == 0 and x % 400 != 0:
    print("NO")
else:
    print("YES")
