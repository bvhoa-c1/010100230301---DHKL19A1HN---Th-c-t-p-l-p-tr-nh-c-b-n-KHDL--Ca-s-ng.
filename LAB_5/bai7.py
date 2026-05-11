s = input("Nhap chuoi: ")

lower = upper = digit = special = 0

for ch in s:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

print("Chu thuong:", lower)
print("Chu hoa:", upper)
print("Chu so:", digit)
print("Ky tu dac biet:", special)