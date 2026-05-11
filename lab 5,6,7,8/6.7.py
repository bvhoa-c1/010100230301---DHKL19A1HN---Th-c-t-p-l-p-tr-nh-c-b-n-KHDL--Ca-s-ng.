# Bai 6.7

m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

matrix = []

for i in range(m):
    row = list(map(int, input(f"Nhap hang {i + 1}: ").split()))
    matrix.append(row)

total = 0

for row in matrix:
    total += sum(row)

print("Tong ma tran:", total)