list_ten: range = range(10, 60, 10)
for x in reversed(list_ten):
    print(x, end=', ')

# Не работает при использовании range
#list_ten = list_ten[::-1]
#print(list_ten)