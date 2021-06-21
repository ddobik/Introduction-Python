stars = []
x = int(input('Enter number of stars: '))
for i in range(x):
    if i <= x:
        i += 1
        stars.append(i)

for i in range(x):
    stars[i] = '*'
#print(*stars)
for elem in stars:
    print(elem, end='')
