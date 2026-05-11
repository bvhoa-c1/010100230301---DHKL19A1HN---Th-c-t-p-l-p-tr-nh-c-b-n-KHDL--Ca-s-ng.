#7.1
n = int(input("Nhập N: "))
d = {}
for x in range(1, n + 1):
    d[x] = x**3
print(d)


#7.2
n = int(input("Nhập số sinh viên: "))

sv = {}

for i in range(n):
    ten = input("Tên: ")
    diem = float(input("Điểm: "))

    if diem >= 8:
        loai = "A"
    elif diem >= 6.5:
        loai = "B"
    elif diem >= 5:
        loai = "C"
    else:
        loai = "F"

    sv[ten] = loai

print(sv)


#7.3
sv = {
    "An": "A",
    "Bình": "B",
    "Cường": "A",
    "Dung": "C"
}

dem = {}

for x in sv.values():
    dem[x] = dem.get(x, 0) + 1

print(dem)



#7.4
text = input("Nhập đoạn văn: ")

text = text.lower()

words = text.split()

dem = {}

for w in words:
    dem[w] = dem.get(w, 0) + 1

print(dem)



#7.5
d = {
    "apple": 5,
    "banana": 2,
    "cat": 7,
    "dog": 2
}

max_word = max(d, key=d.get)
min_word = min(d, key=d.get)

print("Nhiều nhất:", max_word)
print("Ít nhất:", min_word)


#7.6
inventory = {
    "gold": 500,
    "backpack": ["dao", "ao", "banh"]
}

inventory["pocket"] = ["day", "keo"]

inventory["gold"] += 50

print(inventory)


#7.7
inventory = {
    "backpack": ["banana", "apple", "book"]
}

inventory["backpack"].sort()

inventory["backpack"].remove("apple")

print(inventory)


#7.8
soluong = {
    "Táo": 2,
    "Cam": 3
}

dongia = {
    "Táo": 10000,
    "Cam": 15000
}

tong = 0

for sp in soluong:
    tien = soluong[sp] * dongia[sp]
    tong += tien

    print(sp, ":", tien)

print("Tổng tiền:", tong)


#7.9
kho = {
    "Táo": 10,
    "Cam": 8
}

ban = {
    "Táo": 3,
    "Cam": 2
}

for sp in ban:
    kho[sp] -= ban[sp]

print("Kho sau khi bán:")
print(kho)


#7.10
kho = {"Táo", "Cam", "Xoài", "Nho"}

mua = {"Táo", "Nho"}

con_lai = kho - mua

print("Sản phẩm chưa mua:")
print(con_lai)