a = []
x = int(input('Введите целое число:'))
while x != 0:
    a.append(x)
    x = int(input('Введите целое число:'))
print(a)
print('Количество введённых чисел:', len(a))
print('Сумма введённых чисел:', sum(a))

p = 1
for item in a:
    p *= item
print('Произведение введённых чисел:', p)
print('Среднее арифметическое введённых чисел:', sum(a) / len(a))

print('Наибольшее значение:', max([item for item in a]))
print('Порядковый номер наибольшего значения:', a.index(max([item for item in a])) + 1)

b = 0
с = 0
for item in a:
    if item % 2 == 0:
        b += 1
    else:
        с += 1
print('Количество чётных чисел:', b)
print('Количество нечётных чисел:', с)

s = sorted(a, reverse=True)
for item1 in s:
    if item1 < s[0]:
        print('Значение второго по величине элемента:', item1)
        break

print('Количество элементов с наибольшим значением:', a.count(max([item for item in a])))
