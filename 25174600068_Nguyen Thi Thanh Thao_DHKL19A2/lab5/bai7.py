s = input("Nhap chuoi: ")

thuong = hoa = so = dacbiet = 0

for ch in s:
    if ch.islower():
        thuong += 1
    elif ch.isupper():
        hoa += 1
    elif ch.isdigit():
        so += 1
    else:
        dacbiet += 1

print("Chu thuong:", thuong)
print("Chu hoa:", hoa)
print("Chu so:", so)
print("Ky tu dac biet:", dacbiet)