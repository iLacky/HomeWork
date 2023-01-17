text = 'Very important message'

try:
    print('=' * 10)
    print(text)
except Exception:
    print(f'Oops! You have little problem')

finally:
    print('=' * 10)
