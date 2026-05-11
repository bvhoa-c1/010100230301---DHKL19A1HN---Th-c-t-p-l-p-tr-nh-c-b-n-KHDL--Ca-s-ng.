n = int(input("Nhập cấp ma trận: "))
A = []
print("Nhập ma trận")
for i in range(n):
    hang = []
    for j in range(n):
        x = float(input(f"A[{i}][{j}] bằng: "))    
    A.append(hang)
I = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    I.append(hang)
for i in range(n):
    A[i]=A[i]+I[i]
for i in range(n):
    if A[i][j]==0:
        print("Ma trận không khả nghịch")
        break
    chia = A[i][j]
    for j in range(2*n):
        A[i][j] = A[i][j] / chia
    for k in range(n):
        if k!= i:
            he_so = A[k][i]
            for j in range(2*n):
                A[k][j] = A[k][j] - he_so * A[i][j]
else:
    print("ma trận nghich đảo là:")
    for i in range(n):
        print(A[i][n:])
