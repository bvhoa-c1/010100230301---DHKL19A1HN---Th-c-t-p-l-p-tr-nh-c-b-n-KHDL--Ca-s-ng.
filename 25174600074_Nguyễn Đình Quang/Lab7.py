# Bài 7.1
n = int(input("Nhập số nguyên N: "))
tu_dien_x3 = {x: x**3 for x in range(1, n + 1)}
print(f"Từ điển kết quả: {tu_dien_x3}")
# Bài 7.2
diem_sinh_vien = {'Trong': 92, 'Nam': 85, 'Hoa': 74, 'Binh': 65, 'Lan': 45}
xep_loai = {}

for ten, diem in diem_sinh_vien.items():
    if diem >= 85: loai = 'A'
    elif diem >= 70: loai = 'B'
    elif diem >= 55: loai = 'C'
    elif diem >= 40: loai = 'D'
    else: loai = 'F'
    xep_loai[ten] = loai

for ten, loai in xep_loai.items():
    print(f"Sinh viên {ten}: Loại {loai}")
# Bài 7.3
# Dữ liệu từ điển xếp loại có sẵn
xep_loai = {'Trong': 'A', 'Nam': 'A', 'Hoa': 'B', 'Binh': 'C', 'Lan': 'D'}
tan_suat_hoc_luc = {}

for loai in xep_loai.values():
    tan_suat_hoc_luc[loai] = tan_suat_hoc_luc.get(loai, 0) + 1

for loai, so_luong in tan_suat_hoc_luc.items():
    print(f"Học lực {loai}: {so_luong} sinh viên")
# Bài 7.4
van_ban = "Python is great! Python is easy to learn."
van_ban_sach = van_ban.lower().replace("!", "").replace(".", "")

danh_sach_tu = van_ban_sach.split()
tu_dien_dem = {}

for tu in danh_sach_tu:
    tu_dien_dem[tu] = tu_dien_dem.get(tu, 0) + 1

print("Tần suất từ vựng:", tu_dien_dem)
# Bài 7.5
# Từ điển tần suất có sẵn
tu_dien_dem = {'python': 2, 'is': 2, 'great': 1, 'easy': 1, 'to': 1, 'learn': 1}

max_count = max(tu_dien_dem.values())
min_count = min(tu_dien_dem.values())

tu_max = [tu for tu, count in tu_dien_dem.items() if count == max_count]
tu_min = [tu for tu, count in tu_dien_dem.items() if count == min_count]

print(f"Từ xuất hiện nhiều nhất: {', '.join(tu_max)}")
print(f"Từ xuất hiện ít nhất: {', '.join(tu_min)}")
# Bài 7.6
inventory = {'gold': 500, 'backpack': ['dagger', 'bedroll']}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['gold'] += 50

print(inventory)
# Bài 7.7
inventory = {'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

inventory['backpack'].sort()
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')

print(inventory['backpack'])
# Bài 7.8
prices = {"banana": 4.5, "apple": 2.0, "orange": 1.5, "pear": 3.0}
stock = {"banana": 15, "apple": 0, "orange": 32, "pear": 10}

total_value = 0
for item in prices:
    chi_phi = prices[item] * stock[item]
    print(f"{item.capitalize()}: ${chi_phi}")
    total_value += chi_phi

print(f"Tổng giá trị: ${total_value}")
# Bài 7.9
stock = {"banana": 15, "orange": 32, "pear": 10}
giao_dich_mua = {"banana": 5, "orange": 12, "pear": 2}

for item, so_luong_mua in giao_dich_mua.items():
    if item in stock and stock[item] >= so_luong_mua:
        stock[item] -= so_luong_mua

print("Tồn kho sau giao dịch:", stock)
# Bài 7.10
danh_muc_kho = {"Laptop", "Chuột", "Bàn phím", "Màn hình", "Tai nghe"}
danh_muc_da_mua = {"Chuột", "Tai nghe", "Bàn phím"}

chua_duoc_mua = danh_muc_kho - danh_muc_da_mua
print("Các mặt hàng chưa được mua:", chua_duoc_mua)
