m = int(input("Nhap so hang ma tran A: "))
n = int(input("Nhap so cot ma tran A: "))

A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

p = int(input("Nhap so hang ma tran B: "))
q = int(input("Nhap so cot ma tran B: "))

B = []
for i in range(p):
    row = list(map(int, input().split()))
    B.append(row)

if n != p:
    print("Khong the nhan hai ma tran")
else:
    C = []

    for i in range(m):
        row = []
        for j in range(q):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            row.append(s)
        C.append(row)

    print("Ma tran tich:")

    for row in C:
        print(row)