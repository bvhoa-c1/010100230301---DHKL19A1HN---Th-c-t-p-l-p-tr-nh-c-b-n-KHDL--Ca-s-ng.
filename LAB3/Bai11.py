n = int(input("Bạn muốn in bao nhiêu số Fibonacci? "))

a, b = 0, 1
print(f"{n} số Fibonacci đầu tiên là:")

for _ in range(n):
    print(a, end=" ")
    # Cập nhật: a lấy giá trị của b, b lấy giá trị tổng a + b
    a, b = b, a + b