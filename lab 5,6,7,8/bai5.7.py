
s = input("Nhap chuoi: ")

lowercase = 0
uppercase = 0
digits = 0
special = 0

for ch in s:
    if ch.islower():
        lowercase += 1
    elif ch.isupper():
        uppercase += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1

print("So chu thuong:", lowercase)
print("So chu hoa:", uppercase)
print("So chu so:", digits)
print("So ky tu dac biet:", special)