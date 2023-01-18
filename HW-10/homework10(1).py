text = 'My context manager'
class MyContextManager:
    def __enter__(self):
        print('=' * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Oops! You have little problem: {exc_type}')
        print('=' * 10)
        return True


with MyContextManager():
    print(text)

