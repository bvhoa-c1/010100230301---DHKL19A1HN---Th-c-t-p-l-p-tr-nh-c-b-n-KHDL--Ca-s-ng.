# Nhập số hàng và số cột
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

# Khởi tạo ma trận rỗng
ma_tran = []

# Nhập ma trận
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        hang.append(x)
    ma_tran.append(hang)

# Tính tổng các phần tử
tong = 0

for hang in ma_tran:
    tong += sum(hang)

# In ma trận
print("Ma trận:")
for hang in ma_tran:
    print(hang)

# In tổng
print("Tổng các phần tử trong ma trận là:", tong)