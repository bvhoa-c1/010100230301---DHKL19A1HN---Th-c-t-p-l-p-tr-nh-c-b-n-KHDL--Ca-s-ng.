n = int(input("Nhập n: "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        x = int(input("Nhập số: "))
        hang.append(x)
    A.append(hang)
T = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[j][i])
    T.append(hang)
print("Ma trận chuyển vị:")
for i in T:
    print(i)
if A == T:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")