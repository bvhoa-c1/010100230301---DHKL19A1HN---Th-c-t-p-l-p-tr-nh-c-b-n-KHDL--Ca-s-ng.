n = int(input("Nhập n: "))
# dãy số Fibonacci là một chuỗi số vô hạn bắt đàu bằng 0,1
a, b = 0, 1
i = 0

while i < n:
    a, b = b, a + b
    i += 1

print("Fibonacci thứ", n, "là:", a)