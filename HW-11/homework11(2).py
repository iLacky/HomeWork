from datetime import datetime


class MyCustomException(Exception):
    time = datetime.now()
    exc = f'{Exception} Time: {time}'
    with open('file_exc', 'w+') as file_exc:
        file_exc.write(exc)

if True:
    raise MyCustomException('Custom exception is occured')
