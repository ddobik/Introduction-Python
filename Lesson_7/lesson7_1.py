def convert_string_to_list(funk):
    def wrapper():
        print(funk().split(' '))

    return wrapper


@convert_string_to_list
def some_string():
    string = str(input('Введите строку:'))
    return string


some_string()
