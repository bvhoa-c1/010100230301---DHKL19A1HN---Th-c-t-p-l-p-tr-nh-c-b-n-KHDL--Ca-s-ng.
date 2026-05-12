#Bài 7.1
N = int(input("Nhap N: "))

d = {}
for x in range(1, N + 1):
    d[x] = x ** 3

print(d)


#Bài 7.2
n = int(input("Nhap so sinh vien: "))

sinh_vien = {}

for i in range(n):
    ten = input("Nhap ten: ")
    diem = float(input("Nhap diem: "))

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

    sinh_vien[ten] = loai

print(sinh_vien)


#Bài 7.3
n = int(input("Nhap so sinh vien: "))

sinh_vien = {}

for i in range(n):
    ten = input("Nhap ten: ")
    loai = input("Nhap xep loai A-F: ")
    sinh_vien[ten] = loai

thong_ke = {}

for loai in sinh_vien.values():
    thong_ke[loai] = thong_ke.get(loai, 0) + 1

print("Thong ke:", thong_ke)


#Bài 7.4
text = input("Nhap van ban tieng Anh: ").lower()

for c in ".,!?;:":
    text = text.replace(c, "")

words = text.split()
dem = {}

for w in words:
    dem[w] = dem.get(w, 0) + 1

print(dem)


#Bài 7.5
text = input("Nhap van ban tieng Anh: ").lower()

for c in ".,!?;:":
    text = text.replace(c, "")

words = text.split()
dem = {}

for w in words:
    dem[w] = dem.get(w, 0) + 1

max_count = max(dem.values())
min_count = min(dem.values())

print("Tu xuat hien nhieu nhat:")
for w in dem:
    if dem[w] == max_count:
        print(w)

print("Tu xuat hien it nhat:")
for w in dem:
    if dem[w] == min_count:
        print(w)


#Bài 7.6
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["gold"] += 50

print(inventory)


#Bài 7.7
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["backpack"].sort()
inventory["backpack"].remove("dagger")

print(inventory["backpack"])


#Bài 7.8
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

tong = 0

for item in stock:
    tien = stock[item] * prices[item]
    tong += tien
    print(item, ":", stock[item], "x", prices[item], "=", tien)

print("Tong tien:", tong)


#Bài 7.9
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

mua = {
    "banana": 2,
    "orange": 5,
    "pear": 3
}

for item in mua:
    if item in stock and stock[item] >= mua[item]:
        stock[item] -= mua[item]

print("Ton kho sau khi giao dich:")
print(stock)


#Bài 7.10
kho = {"apple", "banana", "orange", "pear", "mango"}
khach_mua = {"banana", "pear"}

chua_mua = kho - khach_mua

print("San pham co trong kho nhung chua mua:", chua_mua)