# Bài 1: Tìm số Fibonacci thứ n bằng while
n = int(input("Nhập n: "))
if n <= 0:
    print("n phải lớn hơn 0")
else:
    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1
    print(f"Số Fibonacci thứ {n} là {b}")
