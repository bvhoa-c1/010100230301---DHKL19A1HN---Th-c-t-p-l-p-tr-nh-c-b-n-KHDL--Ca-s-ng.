s = input("Nhập xâu: ")

lower = upper = digit = special = 0

for c in s:
    if c.islower():
        lower += 1
    elif c.isupper():
        upper += 1
    elif c.isdigit():
        digit += 1
    else:
        special += 1

print("Chữ thường:", lower)
print("Chữ hoa:", upper)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)