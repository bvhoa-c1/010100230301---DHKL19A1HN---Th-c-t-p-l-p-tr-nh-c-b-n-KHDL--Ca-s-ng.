# Nhập kích thước ma trận A
m = int(input("Nhập số hàng của ma trận A: "))
n = int(input("Nhập số cột của ma trận A: "))

# Nhập ma trận A
A = []
print("Nhập ma trận A:")
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        hang.append(x)
    A.append(hang)

# Nhập kích thước ma trận B
p = int(input("Nhập số hàng của ma trận B: "))
q = int(input("Nhập số cột của ma trận B: "))

# Kiểm tra điều kiện nhân
if n != p:
    print("Không thể nhân hai ma trận!")
else:
    # Nhập ma trận B
    B = []
    print("Nhập ma trận B:")
    for i in range(p):
        hang = []
        for j in range(q):
            x = int(input(f"B[{i}][{j}] = "))
            hang.append(x)
        B.append(hang)

    # Khởi tạo ma trận kết quả
    C = []

    # Nhân ma trận
    for i in range(m):
        hang = []
        for j in range(q):
            tong = 0
            for k in range(n):
                tong += A[i][k] * B[k][j]
            hang.append(tong)
        C.append(hang)

    # In kết quả
    print("Ma trận tích A x B là:")
    for hang in C:
        print(hang)