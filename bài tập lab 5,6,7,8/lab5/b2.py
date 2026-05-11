str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
common = ""
for ch in str1:
    if ch in str2 and ch not in common:
        common += ch
print("Ký tự chung:", common)