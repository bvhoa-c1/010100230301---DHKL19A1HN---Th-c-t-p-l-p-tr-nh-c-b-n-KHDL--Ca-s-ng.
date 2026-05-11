n = int(input("nhập cấp của ma trận vuông: "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] bằng: "))
        hang.append(x)
    A.append(hang)
chuyen_vi = []
for j in range(n):
    hang = []
    for i in range(n):
        hang.append(A[i][j])
    chuyen_vi.append(hang)
print("ma trận chuyển vị")
for hang in chuyen_vi: 
    print(hang)
doi_xung = True
for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            doi_xung = False
            break
if doi_xung:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")