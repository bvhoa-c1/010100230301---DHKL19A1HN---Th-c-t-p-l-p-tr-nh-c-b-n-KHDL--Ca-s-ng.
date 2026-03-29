n = int(input("Nhập n: "))

a = 0
b = 1
i = 1

while i < n:
    c = a + b
    a = b
    b = c
    i += 1

print(f"Số Fibonacci thứ {n} là: {a}")