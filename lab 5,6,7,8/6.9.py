# Bai 6.9

n = int(input("Nhap cap ma tran vuong: "))

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Chuyen vi
transpose = []

for j in range(n):
    row = []

    for i in range(n):
        row.append(matrix[i][j])

    transpose.append(row)

print("Ma tran chuyen vi:")

for row in transpose:
    print(row)

# Kiem tra doi xung
if matrix == transpose:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")