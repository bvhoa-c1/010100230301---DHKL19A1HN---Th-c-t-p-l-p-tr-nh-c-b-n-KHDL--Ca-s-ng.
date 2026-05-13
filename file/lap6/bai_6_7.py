# Bài 6.7: Tính tổng tất cả phần tử trong ma trận m×n

m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))

matrix = []
print(f"\nNhập các phần tử của ma trận {m}×{n}:")

for i in range(m):
    row = []
    for j in range(n):
        num = int(input(f"Phần tử [{i+1}][{j+1}]: "))
        row.append(num)
    matrix.append(row)

# Tính tổng tất cả phần tử
total_sum = sum(sum(row) for row in matrix)

print(f"\nMa trận:")
for row in matrix:
    print(row)

print(f"\nTổng tất cả phần tử: {total_sum}")
