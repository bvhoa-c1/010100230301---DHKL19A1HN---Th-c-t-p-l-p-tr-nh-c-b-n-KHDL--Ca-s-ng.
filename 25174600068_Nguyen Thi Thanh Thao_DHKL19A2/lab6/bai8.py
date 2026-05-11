so_dong_A = int(input("Nhap so dong ma tran A: "))
so_cot_A = int(input("Nhap so cot ma tran A: "))

ma_tran_A = []

for i in range(so_dong_A):
    dong = []

    for j in range(so_cot_A):
        gia_tri = int(input("Nhap gia tri: "))
        dong.append(gia_tri)

    ma_tran_A.append(dong)

so_cot_B = int(input("Nhap so cot ma tran B: "))

ma_tran_B = []

for i in range(so_cot_A):
    dong = []

    for j in range(so_cot_B):
        gia_tri = int(input("Nhap gia tri: "))
        dong.append(gia_tri)

    ma_tran_B.append(dong)

ket_qua = [[0 for j in range(so_cot_B)] for i in range(so_dong_A)]

for i in range(so_dong_A):
    for j in range(so_cot_B):
        for k in range(so_cot_A):
            ket_qua[i][j] += ma_tran_A[i][k] * ma_tran_B[k][j]

print("Ma tran tich:")

for dong in ket_qua:
    print(dong)