m = int(input("Nhập số hàng ma trận A: "))
n = int(input("Nhập số cột ma trận A: "))
A = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] bằng: "))
        hang.append(x)
    A.append(hang)
p = int(input("Nhập số hang B: "))
q = int(input("Nhập số cột B: "))
B = []
for i in range(p):
    hang = []
    for j in range(q):
        x = int(input(f"B[{i}][{j}] bằng: "))
        hang.append(x)
    B.append(hang)
if n != p:
    print("Không thể nhân hai ma trận")
else:
    C = []
    for i in range(m):
        hang = []
        for j in range(q):
            tong = 0
            for k in range(n):
                tong += A[i][j] * B[i][j]
            hang.append(tong)
        C.append(hang)
    print("ma trận tích")
    for hang in C:
        print(hang)