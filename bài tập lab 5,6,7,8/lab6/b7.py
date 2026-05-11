m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Nhập a[{i}][{j}]: ")))
    matrix.append(row)
total = 0
for i in range(m):
    for j in range(n):
        total += matrix[i][j]
print("Tổng ma trận:", total)