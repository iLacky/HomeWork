text = 'Very important message'

try:
    print('=' * 10)
    print(text)
except Exception as exc_text:
    print(f'Oops! You have little problem: {type(exc_text)}')

finally:
    print('=' * 10)
