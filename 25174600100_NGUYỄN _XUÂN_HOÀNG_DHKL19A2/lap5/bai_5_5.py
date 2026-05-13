# Bài 5.5: Trộn hai chuỗi bằng cách lấy lần lượt từng ký tự

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

merged = ""
max_len = max(len(str1), len(str2))

for i in range(max_len):
    if i < len(str1):
        merged += str1[i] + "-"
    if i < len(str2):
        merged += str2[i] + "-"

# Loại bỏ dấu gạch nối cuối cùng
merged = merged.rstrip("-")

print(f"Chuỗi sau khi trộn: {merged}")
