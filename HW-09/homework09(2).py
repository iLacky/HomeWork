try:
    numb = input('Enter the Fibonacci number: ')
    n = int(numb)
    class ItFibonacci:
        n = int(numb)
        f1 = f2 = 1
        def __iter__(self):
            return self

        def __next__(self):
            for i in range(2, self.n):
                self.f1, self.f2 = self.f2, self.f1 + self.f2
            return self.f2
    f_iter = ItFibonacci()
    print(next(f_iter))
except ValueError:
    print('Only numbers are allowed!')
