# bai 1
n = int(input("Nhập số nguyên dương n:"))
nhi_phan = ""
while n > 0:
    du = n % 2
    nhi_phan = str(du) + nhi_phan
    n = n // 2
print("Số nhị phân là:", nhi_phan)
# bai 2
chuoi_1 = input(" nhap chuoi thu nhat:")
chuoi_2 = input(" nhap chuoi thu hai:")
tim_thay = False
for do_dai in range(1, min(len(chuoi_1), len(chuoi_2)) + 1):
    for i in range(len(chuoi_1) - do_dai + 1) :
        chuoi_con = chuoi_1[i:i + do_dai]
        if chuoi_con in chuoi_2:
            print(" chuoi con chung ngan nhat la:", chuoi_con)
            tim_thay = True
            break
    if tim_thay:
        break
if tim_thay == False:
    print(" khong co chuoi con chung")   

# bai 3
van_ban = input(" nhap chuoi van ban:")
tu_khoa = input(" nhap tu khoa:")
danh_sach_tu  = van_ban.split()
print("vi tri xuat hien cua tu khoa:")
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
print(" tu xuat hien nhieu nhat la:", tu_xuat_hien_nhieu_nhat)
print("so lam xuat hien la:", tu_dien_dem[tu_xuat_hien_nhieu_nhat])

#bai 4
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
chuoi = input(" nhap chuoi")  
chuoi_so = ""
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chuoi_so += ky_tu
if chuoi_so == "":
    print(" khong co chu so trong chuoi")
else:
    so = int(chuoi_so)
    print(" so sau khi xu ly la:", so)
    if kiem_tra_so_nguyen_to(so):
        print(" day la so nguyen to")
    else:
        print(" day khong phai la so nguyen to")

# bai 5
chuoi_1 = input(" nhap chuoi 1:")
chuoi_2 = input(" nhap chuoi 2:")
ket_qua = []
do_dai_lon_nhat = max(len(chuoi_1), len(chuoi_2))
for i in range(do_dai_lon_nhat):
    if i < len(chuoi_1):
        ket_qua.append(chuoi_1[i])
    if i < len(chuoi_2):
        ket_qua.append(chuoi_2[i])
print(" chuoi sau khi tron la:")
print("-". join(ket_qua))

# bai 6
chuoi = input(" nhap chuoi")
tu_dien_ky_tu = {}
for ky_tu in chuoi:
    if not ky_tu.isalnum() and ky_tu !="":
        if ky_tu in tu_dien_ky_tu:
            tu_dien_ky_tu[ky_tu] += 1
        else:
            tu_dien_ky_tu[ky_tu] = 1
print(" cac ky tu dac biet:")
for ky_tu in tu_dien_ky_tu:
    phan_tram = (tu_dien_ky_tu[ky_tu] / len(chuoi) * 100)
    print(ky_tu, ":", tu_dien_ky_tu[ky_tu], "lan")
    print("ty le:", round(phan_tram, 2), "%")

# bai 7
chuoi = input(" nhap chuoi")
so_chu_thuong = 0
so_chu_hoa = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
for ky_tu in chuoi :
    if ky_tu.islower():
        so_chu_thuong += 1
    elif ky_tu.isupper():
        so_chu_hoa += 1
    else:
        so_ky_tu_dac_biet += 1
print(" so chu thuong la:", so_chu_thuong)
print("so chu hoa la:", so_chu_hoa)
print(" so ky tu dac biet:", so_ky_tu_dac_biet)
 # bai 8
chuoi = input(" nhap chuoi:")
if len(chuoi) > 10:
    print("chuoi tu vi tri thu 2 den thu 8:")
    print(chuoi[2:9])
    print(" lay 5 ky tu tu vi tri thu 5:")
    print(chuoi[5: 10])
    print(" 3 ky tu cuoi:")
    print(chuoi[-3:])
    print(" chuoi viet hoa:")
    print(chuoi.upper())
    print(" chuoi viet thuong:")
    print(chuoi.lower())
    print(" chuoi dao nguoc:")
    print(chuoi[:: - 1])

# bai 9
chuoi_ban_dau = input(" nhap chuoi ban dau:")
chuoi_muc_tieu = input("nhap chuoi muc tieu:")
if chuoi_ban_dau == chuoi_muc_tieu:
    print(" hai chuoi giong nhau:")
elif abs (len(chuoi_ban_dau) - len(chuoi_muc_tieu)) <= 1:
    print(" co the chuyen doi bang them, xoa hoac thay the ky tu")
else:
    print("kho chuyen doi")
        
# bai 10
chuoi = input(" nhap chuoi:")
chuoi_moi = chuoi.replace("", "")
print("chuoi sau khi xoa khoang trang la:")
print(chuoi_moi)