# Nhập số nguyên N, tạo từ điển có khóa x và giá trị x^3

N = int(input("Nhập N: "))

data = {}

for x in range(1, N + 1):
    data[x] = x ** 3

print(data)