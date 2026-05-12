s = input("Nhập chuỗi: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("Chuỗi sau xử lý:", result)