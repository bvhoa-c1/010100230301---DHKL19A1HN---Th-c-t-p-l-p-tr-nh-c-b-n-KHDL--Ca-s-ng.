#Bài 7.1


n = int(input("Nhap N: "))

d = {}

for x in range(1, n+1):

    d[x] = x**3


print(d)
#Bài 7.2


n = int(input("Nhap so sinh vien: "))

students = {}


for i in range(n):

    name = input("Nhap ten: ")
    score = float(input("Nhap diem: "))


    if score >= 8:

        grade = "A"

    elif score >= 7:

        grade = "B"

    elif score >= 6:

        grade = "C"

    elif score >= 5:

        grade = "D"

    else:

        grade = "F"


    students[name] = grade


print("Ket qua:")

for name in students:

    print(name, students[name])
#Bài 7.3

freq = {}


for grade in students.values():

    if grade not in freq:

        freq[grade] = 1

    else:

        freq[grade] += 1


print(freq)
#Bài 7.4

text = input("Nhap van ban: ")

words = text.lower().split()

freq = {}


for word in words:

    if word not in freq:

        freq[word] = 1

    else:

        freq[word] += 1


print(freq)
#Bài 7.5


max_count = max(freq.values())
min_count = min(freq.values())


print("Xuat hien nhieu nhat:")

for word in freq:

    if freq[word] == max_count:

        print(word, freq[word])


print("Xuat hien it nhat:")

for word in freq:

    if freq[word] == min_count:

        print(word, freq[word])
#Bài 7.6


inventory = {}


gold = int(input("Nhap gold: "))

inventory["gold"] = gold


n = int(input("So vat trong backpack: "))

backpack = []


for i in range(n):

    item = input("Nhap vat pham: ")

    backpack.append(item)


inventory["backpack"] = backpack


m = int(input("So vat trong pocket: "))

pocket = []


for i in range(m):

    item = input("Nhap vat pham: ")

    pocket.append(item)


inventory["pocket"] = pocket


add_gold = int(
    input("Gold them: ")
)

inventory["gold"] += add_gold


print(inventory)
#Bài 7.7


remove_item = input(
    "Vat pham can xoa: "
)


inventory["backpack"].sort()


if remove_item in inventory["backpack"]:

    inventory["backpack"].remove(
        remove_item
    )


print(inventory)
#Bài 7.8


n = int(input("So mat hang: "))

qty = {}
price = {}


for i in range(n):

    name = input("Ten hang: ")

    quantity = int(input("So luong: "))

    cost = float(input("Don gia: "))


    qty[name] = quantity

    price[name] = cost


tong = 0


print("Hoa don:")


for item in qty:

    total = qty[item] * price[item]

    tong += total

    print(item, total)


print("Tong =", tong)
#Bài 7.9
item = input("Ten hang da ban: ")

sold = int(input("So luong ban: "))


if item in qty:

    qty[item] -= sold


print("Ton kho:")

print(qty)
#Bài 7.10
warehouse = set(
    input("Nhap kho: ").split()
)

cart = set(
    input("Nhap gio hang: ").split()
)


remain = warehouse - cart


print("Chua mua:")

print(remain)