s = input("Nhap chuoi: ")

special = {}
total = len(s)

for ch in s:
    if not ch.isalnum() and ch != " ":
        special[ch] = special.get(ch, 0) + 1

print("Tan suat ky tu dac biet:")

for k, v in special.items():
    percent = (v / total) * 100
    print(k, ":", v, "lan -", round(percent, 2), "%")