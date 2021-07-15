def square(x):
    import math
    p = x * 4
    s = x ** 2
    d = math.sqrt(x ** 2 * 2)
    k = (p, s, d)
    print(k)


a = int(input('Ввведите длину стороны квадрата:'))
square(a)
