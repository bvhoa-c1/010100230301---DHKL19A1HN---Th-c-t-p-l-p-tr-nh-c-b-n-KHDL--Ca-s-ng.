

n = int(input("Nhap n: "))

fib = [0, 1]

[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]

print("Day Fibonacci:")
print(fib[:n])