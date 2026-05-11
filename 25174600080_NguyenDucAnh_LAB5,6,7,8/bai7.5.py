# Nhập đoạn văn bản
van_ban = input("Nhập đoạn văn tiếng Anh: ")

# Chuyển về chữ thường
van_ban = van_ban.lower()

# Xóa dấu câu
for ky_tu in ".,!?;:()[]{}\"'":
    van_ban = van_ban.replace(ky_tu, "")

# Tách từ
danh_sach_tu = van_ban.split()

# Đếm số lần xuất hiện của từ
tan_suat = {}

for tu in danh_sach_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

# Tìm tần suất lớn nhất và nhỏ nhất
max_lan = max(tan_suat.values())
min_lan = min(tan_suat.values())

# Tìm các từ có tần suất cao nhất
tu_max = []
for tu, so_lan in tan_suat.items():
    if so_lan == max_lan:
        tu_max.append(tu)

# Tìm các từ có tần suất thấp nhất
tu_min = []
for tu, so_lan in tan_suat.items():
    if so_lan == min_lan:
        tu_min.append(tu)

# In kết quả
print("\nTần suất xuất hiện của các từ:")
for tu, so_lan in tan_suat.items():
    print(tu, ":", so_lan)

print("\nTừ xuất hiện nhiều nhất:")
for tu in tu_max:
    print(tu, ":", max_lan, "lần")

print("\nTừ xuất hiện ít nhất:")
for tu in tu_min:
    print(tu, ":", min_lan, "lần")