# Thống kê các loại ký tự trong chuỗi

s = input("Nhập chuỗi: ")

lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0

# Duyệt từng ký tự
for ch in s:

    if ch.islower():
        lower_count += 1

    elif ch.isupper():
        upper_count += 1

    elif ch.isdigit():
        digit_count += 1

    # Không tính khoảng trắng là ký tự đặc biệt
    elif ch != " ":
        special_count += 1

# Hiển thị kết quả
print("Số chữ thường:", lower_count)
print("Số chữ in hoa:", upper_count)
print("Số chữ số:", digit_count)
print("Số ký tự đặc biệt:", special_count)