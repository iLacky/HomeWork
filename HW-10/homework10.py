def MyDec(func):
    from datetime import datetime

    def wrap(*args, **kwargs):
        time = datetime.now()
        print(f'Open function: {func} \n Time: {time}')
        func(12, 'test', {'key': '1'})
    return wrap

@MyDec
def my_func(*args, **kwargs):
    print(*args, **kwargs)
my_func()
