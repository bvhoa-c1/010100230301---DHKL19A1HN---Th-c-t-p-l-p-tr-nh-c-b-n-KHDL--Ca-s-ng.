m1 = int(input("Ma trận 1 - số hàng: "))
n1 = int(input("Ma trận 1 - số cột: "))
m2 = int(input("Ma trận 2 - số hàng: "))
n2 = int(input("Ma trận 2 - số cột: "))
if n1 != m2:
    print("Không thể nhân ma trận")
else:
    A = []
    for i in range(m1):
        row = []
        for j in range(n1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)
    B = []
    for i in range(m2):
        row = []
        for j in range(n2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)
    C = []
    for i in range(m1):
        row = [0]*n2
        C.append(row)
    for i in range(m1):
        for j in range(n2):
            s = 0
            for k in range(n1):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    print("Ma trận tích:")
    for row in C:
        print(row)