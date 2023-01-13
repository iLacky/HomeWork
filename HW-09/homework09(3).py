while True:
    try:
        number = input('Enter the Fibonacci number: ')
        num = int(number)
        def fibonacci(num):
            if num in (1, 2):
                return 1
            return fibonacci(num - 1) + fibonacci(num - 2)


        print(fibonacci(num))
    except Exception:
        print('Only numbers are allowed!')


