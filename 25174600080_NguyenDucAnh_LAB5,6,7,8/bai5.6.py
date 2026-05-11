# Đếm ký tự đặc biệt và tính tỉ lệ %

s = input("Nhập chuỗi: ")

special_count = {}
length = len(s)

# Duyệt từng ký tự trong chuỗi
for ch in s:

    # Kiểm tra ký tự đặc biệt
    if not ch.isalnum() and ch != " ":

        if ch in special_count:
            special_count[ch] += 1
        else:
            special_count[ch] = 1

# Hiển thị kết quả
if len(special_count) == 0:
    print("Không có ký tự đặc biệt.")
else:
    print("Thống kê ký tự đặc biệt:")

    for ch in special_count:
        count = special_count[ch]
        percent = (count / length) * 100

        print(f"Ký tự '{ch}' xuất hiện {count} lần - {percent:.2f}%")