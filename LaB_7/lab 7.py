# Bài 7.1
# Tạo dictionary với giá trị là x^3

n = int(input("Nhập N: "))

d = {}

for x in range(1, n + 1):
    d[x] = x ** 3

print(d)
# Bài 7.2
# Xếp loại sinh viên

n = int(input("Nhập số sinh viên: "))

sv = {}

for i in range(n):
    ten = input("Nhập tên: ")
    diem = float(input("Nhập điểm: "))

    if diem >= 8.5:
        loai = "A"
    elif diem >= 7:
        loai = "B"
    elif diem >= 5.5:
        loai = "C"
    elif diem >= 4:
        loai = "D"
    else:
        loai = "F"

    sv[ten] = loai

print(sv)

# Bài 7.3
# Đếm số lượng từng loại học lực

hocluc = {
    "An": "A",
    "Bình": "B",
    "Lan": "A",
    "Nam": "C",
    "Hoa": "B"
}

dem = {}

for x in hocluc.values():
    if x in dem:
        dem[x] += 1
    else:
        dem[x] = 1

print(dem)

# Bài 7.4
# Đếm số lần xuất hiện của từ

text = input("Nhập đoạn văn: ")

text = text.lower()
words = text.split()

dem = {}

for w in words:
    if w in dem:
        dem[w] += 1
    else:
        dem[w] = 1

print(dem)

# Bài 7.5
# Tìm từ xuất hiện nhiều nhất và ít nhất

text = input("Nhập đoạn văn: ")

words = text.lower().split()

dem = {}

for w in words:
    if w in dem:
        dem[w] += 1
    else:
        dem[w] = 1

max_word = max(dem, key=dem.get)
min_word = min(dem, key=dem.get)

print("Từ nhiều nhất:", max_word)
print("Từ ít nhất:", min_word)

# Bài 7.6
# Inventory

inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = ["seashell", "strange berry"]

inventory["gold"] += 50

print(inventory)

# Bài 7.7
# Sắp xếp backpack và xóa vật phẩm

inventory = {
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["backpack"].sort()

inventory["backpack"].remove("dagger")

print(inventory)

# Bài 7.8
# In hóa đơn

soluong = {
    "Táo": 3,
    "Cam": 2,
    "Sữa": 1
}

dongia = {
    "Táo": 10000,
    "Cam": 15000,
    "Sữa": 30000
}

tong = 0

for sp in soluong:
    tien = soluong[sp] * dongia[sp]
    tong += tien

    print(sp, "-", soluong[sp], "-", tien)

print("Tổng tiền:", tong)

# Bài 7.9
# Cập nhật tồn kho

kho = {
    "Táo": 10,
    "Cam": 8,
    "Sữa": 5
}

ban = {
    "Táo": 3,
    "Sữa": 2
}

for sp in ban:
    kho[sp] -= ban[sp]

print("Kho sau cập nhật:")
print(kho)

# Bài 7.10
# Dùng Set

kho = {"Táo", "Cam", "Sữa", "Bánh"}
khach_mua = {"Táo", "Sữa"}

con_lai = kho - khach_mua

print("Hàng chưa mua:")
print(con_lai)

