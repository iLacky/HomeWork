
while True:
    try:
        num = int(input('Enter the Fibonacci number: '))
        def factorial(num):
            if num == 0:
                return 1
            return num * factorial(num - 1)
        print(factorial(num))
    except Exception:
        print('Only numbers are allowed!')