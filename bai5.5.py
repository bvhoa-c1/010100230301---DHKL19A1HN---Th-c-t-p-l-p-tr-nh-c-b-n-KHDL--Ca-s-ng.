# Trộn hai chuỗi ký tự

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

result = ""

# Tìm độ dài lớn nhất
max_len = max(len(str1), len(str2))

for i in range(max_len):

    # Lấy ký tự của str1 nếu còn
    if i < len(str1):
        result += str1[i]

    result += "-"

    # Lấy ký tự của str2 nếu còn
    if i < len(str2):
        result += str2[i]

    # Không thêm dấu "-" ở cuối
    if i != max_len - 1:
        result += "-"

print("Chuỗi sau khi trộn:", result)