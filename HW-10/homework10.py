def MyDec(func):
    from datetime import datetime

    def wrap(*args, **kwargs):
        time = datetime.now()
        result = func(*args, **kwargs)
        print(f'Open function: {func} \n Time: {time}')
        return result
    return wrap

@MyDec
def my_func(*args, **kwargs):
    print(*args, **kwargs)
my_func()
