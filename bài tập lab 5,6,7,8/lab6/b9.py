n = int(input("Nhập cấp ma trận: "))
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)
T = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(A[j][i])
    T.append(row)
print("Ma trận chuyển vị:")
for row in T:
    print(row)
symmetric = True
for i in range(n):
    for j in range(n):
        if A[i][j] != T[i][j]:
            symmetric = False
            break
if symmetric:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")