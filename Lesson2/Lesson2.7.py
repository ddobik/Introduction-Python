stars = []
x = int(input('Enter number of stars: '))
for element in range(x):
    if element <= x:
        element += 1
        stars.append(element)

for element in range(x):
    stars[element] = '*'
#print(*stars)
for element in stars:
    print(element, end='')