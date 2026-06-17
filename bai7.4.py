# Nhập đoạn văn bản
van_ban = input("Nhập đoạn văn tiếng Anh: ")

# Chuyển về chữ thường
van_ban = van_ban.lower()

# Xóa dấu câu
for ky_tu in ".,!?;:()[]{}\"'":
    van_ban = van_ban.replace(ky_tu, "")

# Tách các từ
danh_sach_tu = van_ban.split()

# Từ điển đếm số lần xuất hiện
tan_suat = {}

# Đếm tần suất từ
for tu in danh_sach_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

# In kết quả
print("\nSố lần xuất hiện của từng từ:")
for tu, so_lan in tan_suat.items():
    print(tu, ":", so_lan)