n = int(input("Nhap cap ma tran vuong: "))

A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Chuyen vi
T = []

for j in range(n):
    row = []
    for i in range(n):
        row.append(A[i][j])
    T.append(row)

print("Ma tran chuyen vi:")

for row in T:
    print(row)

# Kiem tra doi xung
if A == T:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")