# Bài 7.1: Tạo từ điển với khóa x và giá trị x^3
N = int(input("Nhập N: "))

d = {}

for x in range(1, N + 1):
    d[x] = x ** 3

print(d)

