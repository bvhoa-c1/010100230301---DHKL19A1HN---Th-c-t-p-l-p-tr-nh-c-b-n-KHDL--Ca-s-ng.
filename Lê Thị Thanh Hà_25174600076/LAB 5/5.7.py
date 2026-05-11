s = input("Nhập chuỗi: ")

thuong = hoa = so = db = 0

for ch in s:
    if ch.islower():
        thuong += 1
    elif ch.isupper():
        hoa += 1
    elif ch.isdigit():
        so += 1
    else:
        db += 1

print("Chữ thường:", thuong)
print("Chữ hoa:", hoa)
print("Chữ số:", so)
print("Ký tự đặc biệt:", db)