def countdown(funk):
    def wrapper():
        import time
        list1 = [3, 2, 1]
        for n in list1:
            time.sleep(1)
            print(n)
        funk()
    return wrapper

# Вариант_1:
@countdown
def what_time_is_it_now():
    import datetime
    print(datetime.datetime.now().strftime('%H:%M'))


what_time_is_it_now()


# Вариант_2:
def what_time_is_it_now():
    import datetime
    print(datetime.datetime.now().strftime('%H:%M'))


what_time_is_it_now = countdown(what_time_is_it_now)
what_time_is_it_now()
