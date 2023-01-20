import json
from datetime import datetime


class MyCustomException(Exception):
    time = datetime.now()
    exc = f'{Exception} Time: {time}'
    with open(r'C:\HW\HomeWork\HW-11\file_exc', 'x') as file_exc:
        exc = json.dumps(exc)
        file_exc.write(exc)

if True:
    raise MyCustomException('Custom exception is occured')
