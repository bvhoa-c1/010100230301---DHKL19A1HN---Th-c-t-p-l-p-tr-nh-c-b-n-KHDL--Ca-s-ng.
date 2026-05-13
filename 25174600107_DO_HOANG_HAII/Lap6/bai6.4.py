n = int(input("Nhập số hạng đầu tiên của dãy Fibonacci: "))

def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci = [x for x in fib_generator(n)]

print(f"{n} số hạng đầu tiên của dãy Fibonacci: {fibonacci}")
