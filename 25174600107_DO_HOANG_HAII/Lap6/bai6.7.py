m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

matrix = []

print(f"\nNhập các phần tử của ma trận {m}x{n}:")
for i in range(m):
    row = []
    for j in range(n):
        num = float(input(f"Phần tử [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

total_sum = sum(sum(row) for row in matrix)

print(f"\nMa trận:")
for row in matrix:
    print(row)

print(f"\nTổng tất cả các phần tử: {total_sum}")
