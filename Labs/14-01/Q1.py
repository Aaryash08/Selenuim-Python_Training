class Num:
    def __init__(self,n):
        self.n=n
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=self.n:
            val=self.current
            self.current +=1
            return val
        else:
            raise StopIteration

obj=Num(3)

for num in obj:
    print(num)

def fibonacci(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1
fibonacci(5)
for num in fibonacci(5):
    print(num)

print("Using Custom Iterator:")
iterator_obj = Num(5)
for num in iterator_obj:
    print(num)

print("\nUsing Generator (Fibonacci):")
gen_obj = fibonacci(5)
for num in gen_obj:
    print(num)
