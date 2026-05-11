# Loại bỏ khoảng trắng trong chuỗi

s = input("Nhập chuỗi: ")

# Xóa toàn bộ khoảng trắng
result = ""

for ch in s:
    if ch != " ":
        result += ch

print("Chuỗi sau khi loại bỏ khoảng trắng:")
print(result)