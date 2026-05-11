chuoi_1 = input("Nhap chuoi 1: ")
chuoi_2 = input("Nhap chuoi 2: ")

chuoi_chung = ""

tim_thay = False

for ky_tu_1 in chuoi_1:

    for ky_tu_2 in chuoi_2:

        if ky_tu_1 == ky_tu_2:
            chuoi_chung = ky_tu_1
            tim_thay = True
            break

    if tim_thay:
        break

if tim_thay:
    print("Chuoi con chung ngan nhat:", chuoi_chung)
else:
    print("Khong co chuoi con chung")