#Bài7.1:
n = int(input("Nhập số nguyên N: "))
d = {}
for x in range(1, n + 1):
    d[x] = x ** 3
print(f"Từ điển số mũ: {d}")

#Bài7.2:
n = int(input("Nhập số sinh viên: "))
students = {}
for i in range(n):
    name = input("Nhập tên: ")
    score = float(input("Nhập điểm: "))

    if score >= 8.5:
        grade = "A"
    elif score >= 7:
        grade = "B"
    elif score >= 5.5:
        grade = "C"
    elif score >= 4:
        grade = "D"
    else:
        grade = "F"

    students[name] = grade
print(students)

#Bài7.3:
students = {
    "An": "A",
    "Binh": "B",
    "Lan": "A",
    "Hoa": "C",
    "Minh": "B"
}

count = {}

for grade in students.values():

    if grade in count:
        count[grade] += 1
    else:
        count[grade] = 1

print("Thông kê học lực:")

for k, v in count.items():
    print(k, ":", v)

#Bài7.4:
text = input("Nhập đọan văn: ")

text = text.lower()

for c in ",.!?;:":
    text = text.replace(c, "")

words = text.split()

freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

#Bài7.5:
text = input("Nhập văn bản: ")

text = text.lower()

for c in ",.!?;:":
    text = text.replace(c, "")

words = text.split()

freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Từ xuất hiện nhiều nhất:")
print(max_word, "-", freq[max_word], "lan")

print("Từ xuất hiện ít nhất:")
print(min_word, "-", freq[min_word], "lan")

#Bài7.6:
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll"]
}

inventory["pocket"] = ["seashell", "strange berry"]

inventory["gold"] += 50

print(inventory)

#Bài7.7:
inventory = {
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["backpack"].sort()

inventory["backpack"].remove("dagger")

print(inventory["backpack"])

#Bài7.8:
stock = {
    "apple": 5,
    "banana": 3,
    "milk": 2
}

price = {
    "apple": 10000,
    "banana": 5000,
    "milk": 30000
}

total = 0

print("HÓA ĐƠN")

for item in stock:

    cost = stock[item] * price[item]
    total += cost

    print(item, ":", stock[item], "x", price[item], "=", cost)

print("Tổng tiền =", total)

#Bài7.9:
stock = {
    "apple": 10,
    "banana": 8,
    "milk": 5
}

sell = {
    "apple": 3,
    "milk": 2
}

for item in sell:

    if item in stock:
        stock[item] -= sell[item]

print("Tồn kho sau giao dịch:")

for k, v in stock.items():
    print(k, ":", v)

#Bài7.10:
kho_hang = set({"Tivi", "Tủ lạnh", "Máy giặt", "Điều hòa", "Lò vi sóng"})
khach_chon = set({"Tivi", "Máy giặt"})

chưa_mua = kho_hang - khach_chon
print(f"Sản phẩm khách chưa chọn: {chưa_mua}")