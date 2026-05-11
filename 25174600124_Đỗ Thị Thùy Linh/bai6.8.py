m = int(input("Nhap so hang ma tran A: "))
n = int(input("Nhap so cot ma tran A: "))

A = []

print("Nhap ma tran A:")
for i in range(m):
    A.append(list(map(int, input().split())))

p = int(input("Nhap so cot ma tran B: "))

B = []

print("Nhap ma tran B:")
for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0 for j in range(p)] for i in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Tich hai ma tran:")

for row in C:
    print(row)