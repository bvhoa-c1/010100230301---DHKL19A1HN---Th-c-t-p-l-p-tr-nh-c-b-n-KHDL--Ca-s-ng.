#7.1
n = int(input())
d = {}
for x in range(1, n+1):
    d[x] = x**3
print(d)
#7.2
def classify(score):
    if score >= 9:
        return "A"
    elif score >= 8:
        return "B"
    elif score >= 7:
        return "C"
    elif score >= 6:
        return "D"
    else:
        return "F"
n = int(input("Nhập số sinh viên: "))
students = {}
for i in range(n):
    name = input("Tên sinh viên: ")
    score = float(input("Điểm: "))
    students[name] = score
print("\nKẾT QUẢ")
for name, score in students.items():
    print(name, "-", score, "-", classify(score))
#7.3
def classify(score):
    if score >= 9:
        return "A"
    elif score >= 8:
        return "B"
    elif score >= 7:
        return "C"
    elif score >= 6:
        return "D"
    else:
        return "F"
students = {
    "An": 9,
    "Binh": 8,
    "Lan": 7,
    "Hoa": 5
}
count = {}
for score in students.values():
    rank = classify(score)
    count[rank] = count.get(rank, 0) + 1
print(count)
#7.4
text = input("Nhập văn bản: ")
text = text.lower()
for c in ",.!?":
    text = text.replace(c, "")
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)
#7.5
freq = {
    "hello": 3,
    "world": 1,
    "python": 2
}
max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)
print("Nhiều nhất:", max_word)
print("Ít nhất:", min_word)
#7.6
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["pocket"] = ["seashell", "strange berry"]
inventory["gold"] += 50
print(inventory)
#7.7
inventory = {
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
print(inventory)
#7.8
stock = {
    "apple": 5,
    "banana": 3
}
price = {
    "apple": 10,
    "banana": 7
}
total = 0
for item in stock:
    cost = stock[item] * price[item]
    total += cost
    print(item, "-", cost)
print("Tổng:", total)
#7.9
stock = {
    "apple": 10,
    "banana": 5
}
sold = {
    "apple": 2,
    "banana": 1
}
for item in sold:
    stock[item] -= sold[item]
print(stock)
# 7.10
warehouse = {"apple", "banana", "milk", "cake"}
customer = {"banana", "cake"}
remain = warehouse - customer
print(remain)
