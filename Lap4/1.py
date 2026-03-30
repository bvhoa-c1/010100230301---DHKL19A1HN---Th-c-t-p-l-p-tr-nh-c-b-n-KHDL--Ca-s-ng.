n = int(input("Nhập n: "))
a, b = 0, 1
count = 1
if n == 1:
    print("Số Fibonacci thứ 1 là:", a)
else:
    while count < n:
        a, b = b, a + b
        count += 1
    print(f"Số Fibonacci thứ {n} là:", a)