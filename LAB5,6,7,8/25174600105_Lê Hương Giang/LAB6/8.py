m = int(input("Nhập số hàng A: "))
n = int(input("Nhập số cột A: "))
A = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input("Nhập số: "))
        hang.append(x)
    A.append(hang)
p = int(input("Nhập số hàng B: "))
q = int(input("Nhập số cột B: "))
B = []
for i in range(p):
    hang = []
    for j in range(q):
        x = int(input("Nhập số: "))
        hang.append(x)
    B.append(hang)
if n == p:
    C = []
    for i in range(m):
        hang = []
        for j in range(q):
            tong = 0
            for k in range(n):
                tong += A[i][k] * B[k][j]
            hang.append(tong)
        C.append(hang)
    print("Ma trận tích là:")
    for i in C:
        print(i)
else:
    print("Không nhân được")