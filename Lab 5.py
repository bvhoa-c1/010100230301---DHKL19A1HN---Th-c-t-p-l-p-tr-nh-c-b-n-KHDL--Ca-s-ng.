#Bài 5.1:
n = int(input("Nhập số nguyên dương: "))
nhi_phan = ""
while n > 0:
    du = n % 2
    nhi_phan = str(du) + nhi_phan
    n = n // 2
print("Số nhị phân là: ", nhi_phan)

#BÀi 5.2:
chuoi_1 = input("Nhập chuỗi 1: ")
chuoi_2 = input("Nhập chuỗi 2: ")
tim_thay = False
for do_dai in range(1, len(chuoi_1) +1):
    for i in range(len(chuoi_1) - do_dai + 1 ):
        chuoi_con = chuoi_1[i:i + do_dai]
        if chuoi_con in chuoi_2:
            print("chuỗi con chung ngắn nhất là: ", chuoi_con)
            tim_thay = True
            break
    if not tim_thay:
        print("Không có chuỗi con chung ")

#BÀi 5.3:
chuoi = input("Nhập đoạn văn: ")
tu_khoa = input("Nhập từ khóa: ")
vi_tri = chuoi.find(tu_khoa)
if vi_tri != -1:
    print("Từ khóa xuất hiện tại vị trí: ", vi_tri)
else:
    print("Không tìm thấy từ khóa")
ds_tu = chuoi.split()
tu_nhieu_nhat = ""
so_lan_nhieu_nhat = 0
for tu in ds_tu:
    so_lan = ds_tu.count(tu)
    if so_lan > so_lan_nhieu_nhat:
        so_lan_nhieu_nhat = so_lan
        tu_nhieu_nhat = tu
print("từ xuất hiện nhiều nhất là: ", tu_nhieu_nhat)
print("Số lần xuất hiện: ", so_lan_nhieu_nhat)

#Bài 5.4:
chuoi = input("Nhập chuỗi: ")
chuoi_so = ""
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chuoi_so += ky_tu
print("Chuỗi chỉ gồm số: ", chuoi_so)
if chuoi_so != "":
    so = int(chuoi_so)
    la_nguyen_to = True
    if so < 2:
       la_nguyen_to = False
    else:
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
               la_nguyen_to = False
               break
    if la_nguyen_to:
        print(so, "Là số nguyên tố")
    else:
        print(so, "Không phải số nguyên tố")
else:
    print("Lỗi: không tìm thấy chứ số nào trong chuỗi")

#BÀi 5.5:
chuoi1 = input("Nhập chuỗi 1: ")
chuoi2 = input("Nhập chuỗi 2: ")
ket_qua = ""
do_dai_lon_nhat = max(len(chuoi1), len(chuoi2))
for i in range(do_dai_lon_nhat):
    if i < len(chuoi1):
        ket_qua += chuoi1[i] + "-"
    if i < len(chuoi2):
        ket_qua += chuoi2[i] + "-"
print("Chuỗi sau khi trộn:")
print(ket_qua)

#Bài 5.6:
chuoi = input("Nhập chuỗi: ")
tong_ky_tu = len(chuoi)
da_dem = ""
for ky_tu in chuoi:
    if not ky_tu.isalnum() and ky_tu != "" and ky_tu not in da_dem:
        so_lan = chuoi.count(ky_tu)
        ty_le = (so_lan / tong_ky_tu) * 100
        print(ky_tu, "Xuất hiện", so_lan, "Lần")
        print("Tỷ lệ", round(ty_le, 2), "%")
        da_dem += ky_tu

#Bài 5.7:
chuoi = input("Nhập chuỗi: ")
chu_thuong = 0
chu_hoa = 0
chu_so = 0
ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.islower():
        chu_thuong += 1
    elif ky_tu.isupper():
        chu_hoa += 1
    elif ky_tu.isdigit():
        chu_so += 1
    else:
        ky_tu_dac_biet += 1
print("Số chữ thường : ", chu_thuong)
print("Số chữ hoa: ", chu_hoa)
print("Số chữ số: ", chu_so)
print("Số ký tự đặc biệt: ", ky_tu_dac_biet)

#Bài 5.8:
chuoi = input("Nhập chuỗi lớn hơn 10 ký tự: ")
if len(chuoi) <= 10:
    print("Chuỗi không hợp lệ")
else:
    print("Từ vị trí 2 đến 8: ", chuoi[2:9])
    print("5 ký tự từ vị trí 5: ", chuoi[5:10])
    print("3 ký tư cuỗi: ", chuoi[-3:])
    print("Chuỗi in  thường: ", chuoi.lower())
    print("Chuỗi in hoa: ", chuoi.upper())
    print("Chuỗi đảo ngược: ", chuoi[::-1])

#Bài 5.9:
chuoi_ban_dau = input("Nhập chuỗi ban đầu: ")
chuoi_muc_tieu = input("Nhập chuỗi mục tiêu: ")
if len(chuoi_ban_dau) == len(chuoi_muc_tieu):
    print("Có thể thay thế ký tự")
elif len(chuoi_ban_dau) > len(chuoi_muc_tieu):
    print("Cần xóa ký tự")
else:
    print("Cần thêm ký tự")

#Bài 5.10:
chuoi = input("Nhập chuỗi: ")
ket_qua = ""
for ky_tu in chuoi:

    if ky_tu != " ":
        ket_qua += ky_tu
print("Chuỗi sau khi xóa khoảng trắng:")
print(ket_qua)




