

s = input("Nhap chuoi: ")

special_count = {}
total_length = len(s)

for ch in s:
    if not ch.isalnum() and not ch.isspace():
        special_count[ch] = special_count.get(ch, 0) + 1

print("So lan xuat hien cua ky tu dac biet:")

for ch, count in special_count.items():
    percent = (count / total_length) * 100
    print(f"Ky tu '{ch}': {count} lan - {percent:.2f}%")