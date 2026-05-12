n = int(input("Nhập kích thước ma trận vuông: "))

A = []

for i in range(n):
    row = []

    for j in range(n):
        x = int(input(f"A[{i}][{j}]: "))
        row.append(x)

    A.append(row)

T = []

for j in range(n):
    row = []

    for i in range(n):
        row.append(A[i][j])

    T.append(row)

print("Ma trận chuyển vị:")

for row in T:
    print(row)
