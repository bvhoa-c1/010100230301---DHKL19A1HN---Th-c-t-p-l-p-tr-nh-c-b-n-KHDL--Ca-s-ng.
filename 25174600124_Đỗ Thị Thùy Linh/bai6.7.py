m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

tong = 0

for row in matrix:
    tong += sum(row)

print("Tong ma tran =", tong)