import json
from datetime import datetime


def MyDecFunc(func):
    def wrap():
        time = datetime.now()
        text = f'Open function {func} \n Time: {time}'
        with open(r'C:\HW\HomeWork\HW-11\file_dec', 'x') as file_dec:
            text = json.dumps(text)
            file_dec.write(text)
        func()
    return wrap


@MyDecFunc
def my_func():
    print()

my_func()