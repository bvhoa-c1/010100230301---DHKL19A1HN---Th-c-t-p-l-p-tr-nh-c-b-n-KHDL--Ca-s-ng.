s = input("Nhập xâu: ")
total = len(s)
special = {}
for ch in s:
    if not ch.isalnum():
        if ch in special:
            special[ch] += 1
        else:
            special[ch] = 1
for ch, count in special.items():
    percent = (count / total) * 100
    print(f"'{ch}' xuất hiện {count} lần, chiếm {percent:.2f}%")