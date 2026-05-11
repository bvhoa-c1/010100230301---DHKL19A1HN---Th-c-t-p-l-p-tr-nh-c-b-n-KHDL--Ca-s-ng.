so_dong = int(input("Nhap so dong: "))
so_cot = int(input("Nhap so cot: "))

ma_tran = []

for i in range(so_dong):
    dong = []

    for j in range(so_cot):
        gia_tri = int(input(f"Nhap a[{i}][{j}]: "))
        dong.append(gia_tri)

    ma_tran.append(dong)

tong = 0

for dong in ma_tran:
    tong += sum(dong)

print("Tong cac phan tu trong ma tran:", tong)