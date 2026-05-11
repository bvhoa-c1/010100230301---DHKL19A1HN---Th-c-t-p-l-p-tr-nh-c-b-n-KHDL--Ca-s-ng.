cap_ma_tran = int(input("Nhap cap ma tran: "))

ma_tran = []

for i in range(cap_ma_tran):
    dong = []

    for j in range(cap_ma_tran):
        gia_tri = float(input(f"Nhap a[{i}][{j}]: "))
        dong.append(gia_tri)

    ma_tran.append(dong)

# Tính định thức ma trận 2x2
if cap_ma_tran == 2:
    a = ma_tran[0][0]
    b = ma_tran[0][1]
    c = ma_tran[1][0]
    d = ma_tran[1][1]

    dinh_thuc = a * d - b * c

    if dinh_thuc == 0:
        print("Ma tran khong kha nghich")
    else:
        nghich_dao = [
            [d / dinh_thuc, -b / dinh_thuc],
            [-c / dinh_thuc, a / dinh_thuc]
        ]

        print("Ma tran nghich dao:")

        for dong in nghich_dao:
            print(dong)

else:
    print("Chi ho tro ma tran 2x2")