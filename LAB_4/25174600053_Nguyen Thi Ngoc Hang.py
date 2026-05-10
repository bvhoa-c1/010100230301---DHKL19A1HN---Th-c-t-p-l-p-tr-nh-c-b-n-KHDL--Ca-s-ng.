#bai 1
print("bai 1")
so_n = int(input("Nhap so n: "))
so_truoc, so_sau = 0, 1
bien_dem = 1
while bien_dem < so_n:
    so_truoc, so_sau = so_sau, so_truoc + so_sau
    bien_dem += 1
print(so_truoc)
#bai 2
print("bai 2")
mat_khau_nhap = ""
while mat_khau_nhap != "123456":
    mat_khau_nhap = input("Nhap mat khau: ")
print("Dang nhap thanh cong!")
#bai 3
print("bai 3")
so_nguyen = int(input("Nhap so nguyen: "))
uoc_so = so_nguyen - 1
while uoc_so >= 1:
    if so_nguyen % uoc_so == 0:
        print(uoc_so)
        break
    uoc_so -= 1
#bai 4
print("bai 4")
tong_so = 0
so_luong = 0
so_lon_nhat = None

while True:
    so_vao = int(input("Nhap so: "))
    if so_vao == 0:
        break
    tong_so += so_vao
    so_luong += 1
    if so_lon_nhat is None or so_vao > so_lon_nhat:
        so_lon_nhat = so_vao

print(tong_so)
print(so_luong)
print(so_lon_nhat)
#bai 5
print("bai 5")
so_a = int(input("Nhap so a: "))
chuoi_so = str(so_a)
so_mu = len(chuoi_so)
tong_luy_thua = 0
bien_tam = so_a
while bien_tam > 0:
    chu_so = bien_tam % 10
    tong_luy_thua += chu_so ** so_mu
    bien_tam //= 10
print(so_a == tong_luy_thua)
#bai 6
print("bai 6")
hang = 1
while hang <= 10:
    cot = 2
    while cot <= 9:
        print(f"{cot}x{hang}={hang*cot}", end="\t")
        cot += 1
    print()
    hang += 1
#bai 7
print("bai 7")
n_nhap = int(input("Nhap so: "))
tam = n_nhap
tong_cs = 0
tich_cs = 1
dao_so = 0
while tam > 0:
    don_vi = tam % 10
    print(don_vi)
    tong_cs += don_vi
    tich_cs *= don_vi
    dao_so = dao_so * 10 + don_vi
    tam //= 10
print(tong_cs)
print(tich_cs)
print(dao_so)
#bai 8
print("bai 8")
n_nhap = int(input("Nhap so: "))
tam = n_nhap
tong_cs = 0
tich_cs = 1
dao_so = 0
while tam > 0:
    don_vi = tam % 10
    print(don_vi)
    tong_cs += don_vi
    tich_cs *= don_vi
    dao_so = dao_so * 10 + don_vi
    tam //= 10
print(tong_cs)
print(tich_cs)
print(dao_so)
#bai 9
print("bai 9")
while True:
    print("1. Cong\n2. Tru\n3. Nhan\n4. Chia\n0. Thoat")
    lua_chon = input("Chon thao tac: ")
    if lua_chon == '0':
        break
    if lua_chon in ('1', '2', '3', '4'):
        val1 = float(input("Nhap so thu nhat: "))
        val2 = float(input("Nhap so thu hai: "))
        if lua_chon == '1': print(val1 + val2)
        elif lua_chon == '2': print(val1 - val2)
        elif lua_chon == '3': print(val1 * val2)
        elif lua_chon == '4': print(val1 / val2 if val2 != 0 else "Loi")
#bai 10
print("bai 10")
so_dong = int(input("Nhap so dong: "))
while so_dong > 0:
    print("*" * so_dong)
    so_dong -= 1
#bai 11
print("bai 11")
so_han_che = int(input("Nhap so han che: "))
if so_han_che > 10:
    chay = 1
    t1 = t2 = t3 = t4 = 0
    while chay <= so_han_che:
        t1 += 6**chay
        t2 += 1 / (3**(2*chay + 1))
        t3 += ((-1)**chay) * (chay**2)
        t4 += chay * (chay + 1) * (chay + 2)
        chay += 1
    print(t1)
    print(t2)
    print(t3)
    print(t4)