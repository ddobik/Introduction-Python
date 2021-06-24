list_of_six: range = range(100, 202, 6)
for x in list_of_six:
    if x % 5 == 0 and x<=150:
        print(x, end=', ')


