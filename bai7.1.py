# Nhập số nguyên N
N = int(input("Nhập N: "))

# Khởi tạo từ điển
tu_dien = {}

# Thêm phần tử vào từ điển
for x in range(1, N + 1):
    tu_dien[x] = x ** 3

# In kết quả
print("Từ điển:", tu_dien)