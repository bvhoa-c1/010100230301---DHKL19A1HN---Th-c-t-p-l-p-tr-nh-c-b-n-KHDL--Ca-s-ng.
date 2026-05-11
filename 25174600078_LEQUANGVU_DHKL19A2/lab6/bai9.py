cap_ma_tran = int(input("Nhap cap ma tran: "))

ma_tran = []

for i in range(cap_ma_tran):
    dong = []

    for j in range(cap_ma_tran):
        gia_tri = int(input("Nhap gia tri: "))
        dong.append(gia_tri)

    ma_tran.append(dong)

ma_tran_chuyen_vi = []

for j in range(cap_ma_tran):
    dong = []

    for i in range(cap_ma_tran):
        dong.append(ma_tran[i][j])

    ma_tran_chuyen_vi.append(dong)

print("Ma tran chuyen vi:")

for dong in ma_tran_chuyen_vi:
    print(dong)

if ma_tran == ma_tran_chuyen_vi:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")