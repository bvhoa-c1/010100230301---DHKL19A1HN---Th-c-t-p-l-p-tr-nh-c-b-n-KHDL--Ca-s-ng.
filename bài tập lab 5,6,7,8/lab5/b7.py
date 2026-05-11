s = input("Nhập xâu: ")
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
print("In thường:", lower)
print("In hoa:", upper)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)