s = input("Nhập xâu: ")

special = {}

for c in s:
    if not c.isalnum() and c != ' ':
        special[c] = special.get(c, 0) + 1

for k, v in special.items():
    print(k, ":", v, "lần")
    print("Tỷ lệ:", round(v / len(s) * 100, 2), "%")