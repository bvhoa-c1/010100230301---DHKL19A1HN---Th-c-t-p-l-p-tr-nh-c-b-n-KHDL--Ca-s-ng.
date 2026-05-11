# Nhập số hàng và số cột
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

# Nhập ma trận
A = []

print("Nhập ma trận:")
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        hang.append(x)
    A.append(hang)

# Tạo ma trận chuyển vị
chuyen_vi = []

for j in range(n):
    hang = []
    for i in range(m):
        hang.append(A[i][j])
    chuyen_vi.append(hang)

# In ma trận gốc
print("Ma trận gốc:")
for hang in A:
    print(hang)

# In ma trận chuyển vị
print("Ma trận chuyển vị:")
for hang in chuyen_vi:
    print(hang)

# Kiểm tra đối xứng
if m == n and A == chuyen_vi:
    print("=> Đây là ma trận đối xứng")
else:
    print("=> Đây không phải ma trận đối xứng")