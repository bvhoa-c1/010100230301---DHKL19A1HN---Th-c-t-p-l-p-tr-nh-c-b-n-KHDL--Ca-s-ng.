n = int(input("Nhap n: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print(f"{n} so Fibonacci dau tien:")
print(' '.join(map(str, fib[:n])))

