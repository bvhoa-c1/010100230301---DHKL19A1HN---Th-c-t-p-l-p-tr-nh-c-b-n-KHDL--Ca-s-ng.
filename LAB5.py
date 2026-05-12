# BÀI 5.1
n = int(input("Nhập số nguyên dương n:"))
nhi_phan = ""
while n > 0:
    du = n % 2
    nhi_phan = str(du) + nhi_phan
    n = n // 2
print("Số nhị phân là:", nhi_phan)
# Bài 5.2:
chuoi_1 = input("Nhập chuỗi thứ nhất:")
chuoi_2 = input("Nhập chuỗi thứ hai:")
tim_thay = False
for do_dai in range(1, min(len(chuoi_1), len(chuoi_2)) + 1):
    for i in range(len(chuoi_1) - do_dai + 1):
        chuoi_con = chuoi_1[i:i + do_dai]
        if chuoi_con in chuoi_2:
            print("Chuỗi con chung ngắn nhất là:", chuoi_con)
            tim_thay = True
            break
    if tim_thay:
        break
if tim_thay == False:
    print("Không có chuỗi con chung")
# Bài 5.3:
van_ban = input("Nhập chuỗi văn bản:")
tu_khoa = input("nhập từ khóa:")
danh_sach_tu = van_ban.split()
print("Vị trí xuát hiện của từ khóa:")
for i in range(len(danh_sach_tu)):
    if danh_sach_tu[i] == tu_khoa:
        print(i)
tu_dien_dem = {}
for tu in danh_sach_tu:
    if tu in tu_dien_dem:
        tu_dien_dem[tu] += 1
    else:
        tu_dien_dem[tu] = 1
tu_xuat_hien_nhieu_nhat = max(tu_dien_dem, key= tu_dien_dem.get)
print("Từ xuất hiện nhiều nhất là:", tu_xuat_hien_nhieu_nhat)
print("Số lần xuất hiện là:", tu_dien_dem[tu_xuat_hien_nhieu_nhat])
#Bài 5.4
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
chuoi = input("Nhập chuỗi:")
chuoi_so = ""
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chuoi_so += ky_tu
if chuoi_so == "":
    print("Không có chữ số trong chuỗi")
else:
    so = int(chuoi_so)
    print("Số sau khi xử lý là:", so)
    if kiem_tra_so_nguyen_to(so):
        print("đây là số nguyên tố")
    else:
        print("Đây không phải là số nguyên tố")
# BÀi 5.5:
chuoi_1 = input("Nhập chuỗi 1:")
chuoi_2 = input("Nhập chuỗi 2:")
ket_qua = []
do_dai_lon_nhat = max(len(chuoi_1), len(chuoi_2))
for i in range(do_dai_lon_nhat):
    if i < len(chuoi_1):
        ket_qua.append(chuoi_1[i])
    if i < len(chuoi_2):
        ket_qua.append(chuoi_2[i])
print("Chuỗi sau khi trộn là:")
print("-".join(ket_qua))
# Bài 5.6
chuoi = input("Nhập chuỗi:")
tu_dien_ky_tu = {}
for ky_tu in chuoi:
    if not ky_tu.isalnum() and ky_tu != " ":
        if ky_tu in tu_dien_ky_tu:
            tu_dien_ky_tu[ky_tu] += 1
        else:
            tu_dien_ky_tu[ky_tu] = 1
print("các ký tụ đặc biệt:")
for ky_tu in tu_dien_ky_tu:
    phan_tram = (tu_dien_ky_tu[ky_tu] / len(chuoi) * 100)
    print(ky_tu, ":", tu_dien_ky_tu[ky_tu], "lần")
    print("Tỷ leej;", round(phan_tram, 2), "%")
# Bài 5.7;
chuoi = input("Nhập chuỗi:")
so_chu_thuong = 0
so_chu_hoa = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.islower():
        so_chu_thuong += 1
    elif ky_tu.isupper():
        so_chu_hoa += 1
    elif ky_tu.isdigit():
        so_chu_so += 1
    else:
        so_ky_tu_dac_biet += 1
print("Số chữ thương là:", so_chu_thuong)
print("Số chữ hoa là", so_chu_hoa)
print("Số chữ số là:", so_chu_so)
print("Số ký tự đăch biệt:", so_ky_tu_dac_biet)
# BÀi 5.8:
chuoi = input("Nhập chuỗi:")
if len(chuoi) > 10:
    print("chuỗi từ vị trí thứ 2 đén 8:")
    print(chuoi[2:9])
    print("Lấy 5 ký tự từ vị trí thứ 5:")
    print(chuoi[5:10])
    print("3 ký tự cuối:")
    print(chuoi[-3:])
    print("Chuỗi viết hoa:")
    print(chuoi.upper())
    print("Chuỗi viết thương:")
    print(chuoi.lower())
    print("chuỗi đảo ngược:")
    print(chuoi[::-1])
else:
    print("Chuỗi phải có độ dài lớn hơn 10")
# Bài 5.9
chuoi_ban_dau = input("Nhập chuỗi ban đầu:")
chuoi_muc_tieu = input("Nhập chuỗi mục tiêu:")
if chuoi_ban_dau == chuoi_muc_tieu:
    print("Hai chuỗi giống nhau")
elif abs(len(chuoi_ban_dau) - len(chuoi_muc_tieu)) <= 1:
    print("Có thể chuyển dổi bằng thêm, xóa hoặc hay thế ký tự")
else:
    print("Khó chuyển đổi")
# Bài 5.10
chuoi = input("Nhập chuỗi:")
chuoi_moi = chuoi.replace(" ", "")
print("Chuỗi sau khi xóa khoảng trắng là:")
print(chuoi_so)


