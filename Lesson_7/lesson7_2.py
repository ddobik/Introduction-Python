t = float(input('Введите значение температуры:'))
var = float(input('1: C(Цельсий)\n2: F(Фаренгейт)\n3: K(Кельвин)\nВыберите единицу измерения температуры:'))

if var == 1:
    print('Температура по Цельсию:', t)
    print('Температура по Фаренгейту:', t * 1.8 + 32)
    print('Температура по Кельвину:', t + 273.15)
elif var == 2:
    print('Температура по Фаренгейту:', t)
    print('Температура по Цельсию:', (t - 32) / 1.8)
    print('Температура по Кельвину:', (t - 32) / 1.8 + 273.15)
elif var == 3:
    print('Температура по Кельвину:', t)
    print('Температура по Цельсию:', t - 273.15)
    print('Температура по Фаренгейту:', (t - 273.15) * 1.8 + 32)
else:
    print('Проверьте правильность выбора единицы измерения')