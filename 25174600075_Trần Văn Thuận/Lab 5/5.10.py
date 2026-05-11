chuoi_goc = input("Nhập chuỗi có khoảng trắng: ")
chuoi_moi = " "
for i in chuoi_goc:
    if i != " " and i != "\t": # Ktra cả dấu cách và tab
        chuoi_moi += i
print("Chuoi sau khi lam sach:", chuoi_moi)
