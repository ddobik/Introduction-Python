# 1) Вариант без использования функции
print(dict(enumerate(list(input(str('Ведите стороку:'))))))


# 2) Вариант с использованием функции
def lis_dict(x):
    return dict(enumerate(x))

    # print(dict(enumerate(x)))


l = list(input(str('Ведите стороку:')))
print(lis_dict(l))
