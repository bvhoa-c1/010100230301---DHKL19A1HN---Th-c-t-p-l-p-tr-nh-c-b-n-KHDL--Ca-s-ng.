# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))

# Từ điển lưu tên và điểm
sinh_vien = {}

# Nhập thông tin sinh viên
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i+1}: ")
    diem = float(input("Nhập điểm: "))
    sinh_vien[ten] = diem

# Từ điển lưu xếp loại
xep_loai = {}

for ten, diem in sinh_vien.items():
    if diem >= 8.5:
        loai = 'A'
    elif diem >= 7.0:
        loai = 'B'
    elif diem >= 5.5:
        loai = 'C'
    elif diem >= 4.0:
        loai = 'D'
    else:
        loai = 'F'

    xep_loai[ten] = loai

# Đếm số lượng sinh viên ở từng mức học lực
tan_suat = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for loai in xep_loai.values():
    tan_suat[loai] += 1

# In kết quả
print("\nXếp loại của sinh viên:")
for ten, loai in xep_loai.items():
    print(ten, ":", loai)

print("\nSố lượng sinh viên ở từng mức học lực:")
for loai, so_luong in tan_suat.items():
    print(loai, ":", so_luong)