so_luong = int(input("Nhap n: "))
danh_sach = []

for i in range(so_luong):
    so = int(input("Nhap so: "))
    danh_sach.append(so)

cong_sai = danh_sach[1] - danh_sach[0]

la_cap_so_cong = True

for i in range(1, so_luong - 1):
    if danh_sach[i + 1] - danh_sach[i] != cong_sai:
        la_cap_so_cong = False
        break

if la_cap_so_cong:
    print("Day la cap so cong")
else:
    print("Day khong phai cap so cong")