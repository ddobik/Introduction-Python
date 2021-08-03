x1 = int(input('Enter x1:'))
y1 = int(input('Enter y1:'))
x2 = int(input('Enter x2:'))
y2 = int(input('Enter y2:'))
if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    print('Yes')
elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
    print('Yes')
else:
    print('No')
