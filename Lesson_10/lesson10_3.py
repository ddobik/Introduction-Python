def longest_word(string):
    list1 = string.split(' ')
    print(list1)
    item_length = 0
    longest_item = str()
    for item in list1:
        if len(item) > item_length:
            item_length = len(item)
            longest_item = item
    print(longest_item)


s = input('Введите строку:')
longest_word(s)
