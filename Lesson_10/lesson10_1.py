def count_points(win, draw, loss):
    points = win * 3 + draw
    print('Количество очков:', points)
    return points


w = int(input('Введите количество побед:'))
d = int(input('Введите количество матчей, сыгранных в ничью:'))
n = int(input('Введите количество поражений:'))
count_points(w, d, n)
