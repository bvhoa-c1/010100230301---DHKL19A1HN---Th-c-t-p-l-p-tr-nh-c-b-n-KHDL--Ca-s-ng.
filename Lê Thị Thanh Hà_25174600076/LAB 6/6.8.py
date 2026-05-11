m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

A = []
B = []

print("Nhập ma trận A")
for i in range(m):
    row = []

    for j in range(n):
        x = int(input(f"A[{i}][{j}]: "))
        row.append(x)

    A.append(row)

print("Nhập ma trận B")
for i in range(m):
    row = []

    for j in range(n):
        x = int(input(f"B[{i}][{j}]: "))
        row.append(x)

    B.append(row)

C = []

for i in range(m):
    row = []

    for j in range(n):
        row.append(A[i][j] + B[i][j])

    C.append(row)

print("Ma trận tổng:")

for row in C:
    print(row)

