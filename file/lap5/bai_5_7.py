# Bài 5.7: Thống kê chữ cái in thường, in hoa, chữ số và ký tự đặc biệt

text = input("Nhập xâu: ")

lowercase = 0
uppercase = 0
digits = 0
special = 0

for char in text:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        special += 1

print(f"Chữ cái in thường: {lowercase}")
print(f"Chữ cái in hoa: {uppercase}")
print(f"Chữ số: {digits}")
print(f"Ký tự đặc biệt: {special}")
