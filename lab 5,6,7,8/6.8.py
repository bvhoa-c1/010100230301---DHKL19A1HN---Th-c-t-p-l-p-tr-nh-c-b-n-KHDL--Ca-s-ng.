# Bai 6.8

m = int(input("Nhap so hang ma tran A: "))
n = int(input("Nhap so cot ma tran A: "))

A = []

for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

p = int(input("Nhap so cot ma tran B: "))

B = []

for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# Tao ma tran ket qua
C = [[0 for _ in range(p)] for _ in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Ma tran tich:")

for row in C:
    print(row)