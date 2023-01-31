from datetime import datetime


def MyDecFunc(func):
    def wrap(*args, **kwargs):
        time = datetime.now()
        text = f'Open function {func} \n Time: {time}'
        with open('file_dec', 'w+') as file_dec:
            file_dec.write(text)
        return func(*args, **kwargs)
    return wrap


@MyDecFunc
def my_func():
    print()

my_func()
