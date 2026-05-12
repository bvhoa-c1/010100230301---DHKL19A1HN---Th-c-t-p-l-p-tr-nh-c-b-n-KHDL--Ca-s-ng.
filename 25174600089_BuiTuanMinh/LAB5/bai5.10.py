chuoi = input("nhap chuỗi dữ liệu")
ket_qua= ""
for ky_tu in chuoi:
    if ky_tu != " " and ky_tu != "\t":
        ket_qua += ky_tu
print(chuoi)
print(ket_qua)
