# Bài 7.1
n = int(input("Nhập N: "))
tu_dien = {}
for x in range(1, n + 1):
    tu_dien[x] = x ** 3
print(tu_dien)
# Bài 7.2
so_luong = int(input("Nhập số sinh viên: "))
tu_dien_sinh_vien = {}
for i in range(so_luong):
    ten = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm: "))
    if diem >= 8:
        xep_loai = "A"
    elif diem >= 6.5:
        xep_loai = "B"
    elif diem >= 5:
        xep_loai = "C"
    elif diem >= 3.5:
        xep_loai = "D"
    else:
        xep_loai = "F"
    tu_dien_sinh_vien[ten] = xep_loai
print("Kết quả xếp loại:")
print(tu_dien_sinh_vien)
# Bài 7.3
tu_dien_xep_loai = {
    "An": "A",
    "Bình": "B",
    "Lan": "A",
    "Mai": "C",
    "Hùng": "B"
}
dem = {}
for xep_loai in tu_dien_xep_loai.values():

    if xep_loai in dem:
        dem[xep_loai] += 1
    else:
        dem[xep_loai] = 1
print("Số lượng từng học lực:")
print(dem)
# Bài 7.4
van_ban = input("Nhập đoạn văn: ")
van_ban = van_ban.lower()
danh_sach_tu = van_ban.split()
tu_dien_dem = {}

for tu in danh_sach_tu:

    if tu in tu_dien_dem:
        tu_dien_dem[tu] += 1
    else:
        tu_dien_dem[tu] = 1
print("Số lần xuất hiện của từng từ:")
for tu in tu_dien_dem:
    print(tu, ":", tu_dien_dem[tu])
    # Bài 7.5
tu_dien_dem = {
    "python": 5,
    "java": 2,
    "c++": 1,
    "html": 4
}
tu_nhieu_nhat = max(tu_dien_dem, key=tu_dien_dem.get)
tu_it_nhat = min(tu_dien_dem, key=tu_dien_dem.get)
print("Từ xuất hiện nhiều nhất là:", tu_nhieu_nhat)
print("Số lần:", tu_dien_dem[tu_nhieu_nhat])
print("Từ xuất hiện ít nhất là:", tu_it_nhat)
print("Số lần:", tu_dien_dem[tu_it_nhat])
# Bài 7.6
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["gold"] += 50
print(inventory)
# Bài 7.7
inventory = {
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
print("Danh sách sau khi xử lý:")
print(inventory["backpack"])
# Bai 7.8
so_luong = {
    "Táo": 3,
    "Cam": 2,
    "Xoài": 5
}
don_gia = {
    "Táo": 10000,
    "Cam": 15000,
    "Xoài": 20000
}
tong_tien = 0
print("HÓA ĐƠN")
for mat_hang in so_luong:
    thanh_tien = so_luong[mat_hang] * don_gia[mat_hang]
    tong_tien += thanh_tien
    print(mat_hang)
    print("Số lượng:", so_luong[mat_hang])
    print("Đơn giá:", don_gia[mat_hang])
    print("Thành tiền:", thanh_tien)
print("Tổng tiền:", tong_tien)
# Bài 7.9
ton_kho = {
    "Táo": 10,
    "Cam": 8,
    "Xoài": 15
}
giao_dich = {
    "Táo": 3,
    "Cam": 2
}
for mat_hang in giao_dich:
    ton_kho[mat_hang] -= giao_dich[mat_hang]
print("Tồn kho sau cập nhật:")
print(ton_kho)
# Bài 7.10
kho_hang = {"Táo", "Cam", "Xoài", "Nho"}
khach_mua = {"Táo", "Nho"}
chua_mua = kho_hang - khach_mua
print("Sản phẩm chưa được mua là:")
print(chua_mua)

