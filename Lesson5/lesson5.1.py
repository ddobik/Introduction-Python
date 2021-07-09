def is_prime(x):
    k = 0
    for num in range(2, x):
        if x % num == 0:
            k += 1
    if k == 0:
        print('True')
    else:
        print('False')


#is_prime(87)
