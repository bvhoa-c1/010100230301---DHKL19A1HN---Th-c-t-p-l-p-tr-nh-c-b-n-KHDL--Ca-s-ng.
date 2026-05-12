m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = []

    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        row.append(x)

    matrix.append(row)

tong = 0

for row in matrix:
    tong += sum(row)

print("Tổng các phần tử:", tong)
