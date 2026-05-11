# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))

# Tạo từ điển lưu tên và điểm
sinh_vien = {}

# Nhập thông tin sinh viên
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i+1}: ")
    diem = float(input("Nhập điểm: "))
    sinh_vien[ten] = diem

# Xếp loại học thuật
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

# In kết quả
print("\nKết quả xếp loại:")
for ten in xep_loai:
    print(ten, "- Điểm:", sinh_vien[ten], "- Xếp loại:", xep_loai[ten])