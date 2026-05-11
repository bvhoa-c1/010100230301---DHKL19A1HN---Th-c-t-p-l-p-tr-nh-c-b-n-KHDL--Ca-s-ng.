so_sinh_vien = int(input("Nhap so sinh vien: "))

danh_sach = {}

for i in range(so_sinh_vien):
    ten = input("Nhap ten: ")
    diem = float(input("Nhap diem: "))

    if diem >= 8.5:
        xep_loai = "A"
    elif diem >= 7:
        xep_loai = "B"
    elif diem >= 5.5:
        xep_loai = "C"
    elif diem >= 4:
        xep_loai = "D"
    else:
        xep_loai = "F"

    danh_sach[ten] = xep_loai

print(danh_sach)