x = int(input('First day distance:'))
y = int(input('Required distance:'))
n = 1
while x < y:
    x *= 1.1
    n += 1
print('Day number:', n)
