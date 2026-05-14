N = int(input("Nhập N: "))

my_dict = {}

for x in range(1, N + 1):
    my_dict[x] = x ** 3

print(my_dict)
#bài 7.2
students = {
    "An": 9,
    "Bình": 7,
    "Lan": 5,
    "Hoa": 3
}

for name, score in students.items():
    if score >= 8:
        grade = "A"
    elif score >= 6:
        grade = "B"
    elif score >= 5:
        grade = "C"
    else:
        grade = "F"

    print(name, ":", grade)
# bài 7.3
grades = ["A", "B", "A", "C", "F", "B", "A"]

count = {}

for g in grades:
    count[g] = count.get(g, 0) + 1

print(count)
# bài 7.4
text = input("Nhập đoạn văn: ").lower()

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
# bài 7.5
freq = {
    "apple": 5,
    "banana": 2,
    "orange": 7,
    "grape": 1
}

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Xuất hiện nhiều nhất:", max_word)
print("Xuất hiện ít nhất:", min_word)
# bài 7.6
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = ["seashell", "strange berry", "lint"]

inventory["gold"] += 50

print(inventory)
# bài 7.7
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

