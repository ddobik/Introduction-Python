def odd(x):
    n = 0
    for num in range(len(x)):
        if x[num] % 2 != 0:
            x[num] = 0
            n += 1
    print(x)
    print(n)


some_list = [65, 5, -8, 0, -3, 12, 1]
odd(some_list)
