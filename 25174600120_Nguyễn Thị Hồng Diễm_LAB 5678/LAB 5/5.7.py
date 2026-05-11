chuoi = input("Nhập chuỗi cần thống kê: ")
chu_thuong = 0
chu_hoa = 0
so = 0
ky_tu_db = 0
for ky_tu in chuoi:
    if ky_tu.islower(): #ktra chữ thường
        chu_thuong += 1
    elif ky_tu.isupper(): #ktra chữ hoa
        chu_hoa += 1
    elif ky_tu.isdigit(): # ktra số
        so += 1
    else:
        ky_tu_db += 1
print("Số chữ thường:", chu_thuong)
print("số chữ hoa:", chu_hoa)
print("Số chữ số:", so)
print("số ký tự đặc biệt:", ky_tu_db)