n = int(input("Nhập số sinh viên: "))
ds_sv = {}
for i in range(n):
    ten = input("Nhập tên sin viên: ")
    diem = float(input("Nhập điểm sinh viên: "))
    if diem >= 8.5:
        loai = 'A'
    elif diem >=7:
        loai = 'B'
    elif diem >= 5.5:
        loai = 'C'
    elif diem >= 4:
        loai = "D"
    else:
        loai = 'F'
    ds_sv[ten] = loai
print("Danh sách xếp loại:")
for ten in ds_sv:
    print(ten, ":", ds_sv[ten])