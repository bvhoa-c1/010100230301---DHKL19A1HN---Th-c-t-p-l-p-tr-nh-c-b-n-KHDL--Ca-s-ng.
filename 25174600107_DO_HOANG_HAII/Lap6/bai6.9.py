n = int(input("Nhập kích thước ma trận vuông: "))

matrix = []
print(f"\nNhập các phần tử của ma trận {n}x{n}:")
for i in range(n):
    row = []
    for j in range(n):
        num = float(input(f"Phần tử [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

transpose = [[matrix[i][j] for i in range(n)] for j in range(n)]

print(f"\nMa trận gốc:")
for row in matrix:
    print(row)

print(f"\nMa trận chuyển vị:")
for row in transpose:
    print(row)

is_symmetric = all(matrix[i][j] == transpose[i][j] for i in range(n) for j in range(n))

if is_symmetric:
    print("\nMa trận này là đối xứng")
else:
    print("\nMa trận này không đối xứng")
