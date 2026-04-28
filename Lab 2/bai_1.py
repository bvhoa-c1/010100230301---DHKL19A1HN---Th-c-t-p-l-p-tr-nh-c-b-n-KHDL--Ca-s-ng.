n = int(input("Nhap n: "))
a, b = 0, 1
i = 1

while i < n:
    a, b = b, a + b
    i += 1

print("So Fibonacci thu", n, "la:", a)