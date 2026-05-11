so_luong = int(input("Nhap n: "))
danh_sach = []

for i in range(so_luong):
    gia_tri = float(input("Nhap gia tri: "))
    danh_sach.append(gia_tri)

print("Gia tri lon nhat:", max(danh_sach))
print("Gia tri nho nhat:", min(danh_sach))