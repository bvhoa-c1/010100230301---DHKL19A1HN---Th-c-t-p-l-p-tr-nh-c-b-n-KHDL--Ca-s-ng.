n = int(input("Nhap cap ma tran vuong: "))

A = []

for i in range(n):
    A.append(list(map(int, input().split())))

AT = []

for j in range(n):
    row = []

    for i in range(n):
        row.append(A[i][j])

    AT.append(row)

print("Ma tran chuyen vi:")

for row in AT:
    print(row)

if A == AT:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")