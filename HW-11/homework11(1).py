from datetime import datetime


def MyDecFunc(func):
    def wrap(**kwargs):
        time = datetime.now()
        text = f'Open function {func} \n Time: {time}'
        with open('file_dec', 'x') as file_dec:
            file_dec.write(text)
        func(**kwargs)
        return func
    return wrap


@MyDecFunc
def my_func():
    print()

my_func()
