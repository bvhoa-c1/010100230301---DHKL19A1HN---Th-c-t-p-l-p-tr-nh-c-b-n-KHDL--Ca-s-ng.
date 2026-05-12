#Bài 7.1:
n = int(input("Nhập số n: "))
tu_dien = {}
for x in range(1, n + 1):
    tu_dien[x] = x ** 3
print("Từ điển:")
print(tu_dien)

#Bài 7.2:
so_sinh_vien = int(input("Nhập số sinh viên: "))
sinh_vien = {}
for i in range(so_sinh_vien):
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
    sinh_vien[ten] = xep_loai
print("Danh sách xếp loại:")
print(sinh_vien)

#Bài 7.3:
xep_loai = {
    "An": "A",
    "Bình": "B",
    "Lan": "A",
    "Nam": "C",
    "Hoa": "B"
}
dem = {}
for loai in xep_loai.values():
    if loai in dem:
        dem[loai] += 1
    else:
        dem[loai] = 1
print("Số lượng từng học lực:")
print(dem)

#Bài 7.4:
van_ban = input("Nhập đoạn văn tiếng Anh: ")
van_ban = van_ban.lower()
van_ban = van_ban.replace(".", "")
van_ban = van_ban.replace(",", "")
danh_sach_tu = van_ban.split()
tu_dien = {}
for tu in danh_sach_tu:
    if tu in tu_dien:
        tu_dien[tu] += 1
    else:
        tu_dien[tu] = 1
print("Số lần xuất hiện của từng từ:")
print(tu_dien)

#BÀi 7.5:
tu_dien = {
    "apple": 5,
    "banana": 2,
    "orange": 7,
    "grape": 1
}
lon_nhat = max(tu_dien.values())
nho_nhat = min(tu_dien.values())
print("Từ xuất hiện nhiều nhất:")
for tu, so_lan in tu_dien.items():
    if so_lan == lon_nhat:
        print(tu, "-", so_lan)
print("Từ xuất hiện ít nhất:")
for tu, so_lan in tu_dien.items():
    if so_lan == nho_nhat:
        print(tu, "-", so_lan)

#BÀi 7.6:
inventory = {
    "gold": 500,
    "rope": 10
}
inventory["pocket"] = ["dao", "ban do", "den pin"]
inventory["gold"] += 200
print("Inventory sau khi cập nhật:")
print(inventory)

#BÀi 7.7:
inventory = {
    "backpack": ["kiem", "ao giap", "thuoc", "day"]
}
inventory["backpack"].sort()
inventory["backpack"].remove("day")
print("Danh sách backpack:")
print(inventory["backpack"])

#Bài 7.8:
so_luong = {
    "but": 2,
    "vo": 5,
    "thuoc": 1
}
don_gia = {
    "but": 5000,
    "vo": 10000,
    "thuoc": 15000
}
tong_tien = 0
print("HÓA ĐƠN")
for mat_hang in so_luong:
    thanh_tien = so_luong[mat_hang] * don_gia[mat_hang]
    tong_tien += thanh_tien
    print(mat_hang, "-", thanh_tien, "đ")
print("Tổng tiền:", tong_tien, "đ")

#Bài 7.9:
ton_kho = {
    "but": 20,
    "vo": 15,
    "thuoc": 10
}
ban_ra = {
    "but": 5,
    "vo": 3
}
for mat_hang in ban_ra:
    ton_kho[mat_hang] -= ban_ra[mat_hang]
print("Tồn kho sau khi bán:")
print(ton_kho)

#Bài 7.10:
kho_hang = {
    "but",
    "vo",
    "thuoc",
    "tay",
    "sach"
}
khach_mua = {
    "but",
    "sach"
}
chua_mua = kho_hang - khach_mua
print("Các sản phẩm chưa mua:")
print(chua_mua)