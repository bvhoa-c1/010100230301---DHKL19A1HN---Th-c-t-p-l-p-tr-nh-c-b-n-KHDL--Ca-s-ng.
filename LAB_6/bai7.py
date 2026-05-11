m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"a[{i}][{j}] = ")))
    matrix.append(row)

tong = 0

for row in matrix:
    tong += sum(row)

print("Tong cac phan tu:", tong)