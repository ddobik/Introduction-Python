v = int(input('Enter speed of Vasia: '))
t = int(input('Enter time of movement of Vasya: '))

l = v * t % 100
if v >= 0:
    print(l)
else:
    print(100 + l)
