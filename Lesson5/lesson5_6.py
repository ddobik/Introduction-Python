def del_none(x):
    x1 = {key: value for key, value in x.items() if value is not None}
    print(x1)


dict_ = {1: 'odin', 2: 'dva', 3: None, 'line': [1, 2, 3], 'finish': None}
del_none(dict_)
