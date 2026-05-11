s = input("Nhap chuoi: ")

lower = 0
upper = 0
digit = 0
special = 0

for c in s:

    if c.islower():
        lower += 1

    elif c.isupper():
        upper += 1

    elif c.isdigit():
        digit += 1

    else:
        special += 1

print("Chu thuong:", lower)
print("Chu hoa:", upper)
print("Chu so:", digit)
print("Ky tu dac biet:", special)