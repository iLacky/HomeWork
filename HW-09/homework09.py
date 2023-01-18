num = input("Number Fibonacci: ")
num = int(num)

def my_gen(num):
    fibonacci1 = 1
    fibonacci2 = 1
    item = 0
    while item < num - 2:
        add_fibonacci = fibonacci1 + fibonacci2
        fibonacci1 = fibonacci2
        fibonacci2 = add_fibonacci
        item = item + 1
        result = (f'Element value {fibonacci2}')
        yield result

print(list(my_gen(num))[-1])
