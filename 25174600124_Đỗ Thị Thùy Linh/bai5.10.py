s = input("Nhap chuoi: ")

result = ""

for c in s:
    if c != " ":
        result += c

print("Chuoi sau khi xoa khoang trang:", result)