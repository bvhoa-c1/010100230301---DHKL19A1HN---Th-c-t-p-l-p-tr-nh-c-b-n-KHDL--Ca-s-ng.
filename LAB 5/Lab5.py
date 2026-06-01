#5.1
so_thap_phan = int(input("Nhập số thập phân: "))
nhi_phan = bin(so_thap_phan)[2:]
print("Dạng nhị phân:", nhi_phan)
#5.2
chuoi_1 = input("Nhập chuoi_1: ")
chuoi_2 = input("Nhập chuoi_2: ")
con_chung_nho_nhat = ""

for i in range(len(chuoi_1)):
    for j in range(i, len(chuoi_1)):
        sub = chuoi_1[i:j+1]
        if sub in chuoi_2:
            if not con_chung_nho_nhat or len(sub) < len(con_chung_nho_nhat):
                con_chung_nho_nhat = sub
print("Chuỗi con chung ngắn nhất:", con_chung_nho_nhat)
#5.3
van_ban = input("Nhập văn bản: ")
tu_khoa = input("Nhập từ khóa: ")
danh_sach_tu = van_ban.split()

vi_tri = [i for i in range(len(van_ban)) if van_ban.startswith(tu_khoa, i)]
print("Vị trí xuất hiện:", vi_tri)

dem_tu = {}
for tu in danh_sach_tu:
    dem_tu[tu] = dem_tu.get(tu, 0) + 1
tu_pho_bien = max(dem_tu, key=dem_tu.get)
print(f"Từ xuất hiện nhiều nhất: '{tu_pho_bien}' ({dem_tu[tu_pho_bien]} lần)")
#5.4
chuoi_nhap = input("Nhập chuỗi: ")
chuoi_so = "".join([ky_tu for ky_tu in chuoi_nhap if ky_tu.isdigit()])

if chuoi_so:
    so_nguyen = int(chuoi_so)
    la_so_nguyen_to = so_nguyen > 1 and all(so_nguyen % i != 0 for i in range(2, int(so_nguyen**0.5) + 1))
    print(f"Số trích xuất: {so_nguyen}, Là số nguyên tố: {la_so_nguyen_to}")
else:
    print("Không có chữ số nào.")
#5.5
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
ket_qua_tron = []
do_dai_max = max(len(s1), len(s2))

for i in range(do_dai_max):
    if i < len(s1): ket_qua_tron.append(s1[i])
    if i < len(s2): ket_qua_tron.append(s2[i])
print("-".join(ket_qua_tron))
#5.6
xau = input("Nhập xâu: ")
tong_ky_tu = len(xau)
ky_tu_dac_biet = {}

for kt in xau:
    if not kt.isalnum():
        ky_tu_dac_biet[kt] = ky_tu_dac_biet.get(kt, 0) + 1

for kt, so_luong in ky_tu_dac_biet.items():
    ty_le = (so_luong / tong_ky_tu) * 100
    print(f"Ký tự '{kt}': {so_luong} lần ({ty_le:.2f}%)")
#5.7
chuoi_vao = input("Nhập chuoi: ")
thong_ke = {"thường": 0, "hoa": 0, "số": 0, "đặc biệt": 0}

for kt in chuoi_vao:
    if kt.islower(): thong_ke["thường"] += 1
    elif kt.isupper(): thong_ke["hoa"] += 1
    elif kt.isdigit(): thong_ke["số"] += 1
    else: thong_ke["đặc biệt"] += 1
print("Kết quả thống kê:", thong_ke)
#5.8
xau_goc = input("Nhập xâu (>10 ký tự): ")
if len(xau_goc) > 10:
    print("Từ vị trí 2 đến 8:", xau_goc[2:9])
    print("5 ký tự từ vị trí 5:", xau_goc[5:10])
    print("3 ký tự cuối:", xau_goc[-3:])
    print("Viết hoa:", xau_goc.upper())
    print("Viết thường:", xau_goc.lower())
    print("Đảo ngược:", xau_goc[::-1])
#5.9
nguon = input("Chuỗi nguồn: ")
muc_tieu = input("Chuỗi mục tiêu: ")
m, n = len(nguon), len(muc_tieu)
bang = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1): bang[i][0] = i
for j in range(n + 1): bang[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if nguon[i-1] == muc_tieu[j-1]:
            bang[i][j] = bang[i-1][j-1]
        else:
            bang[i][j] = 1 + min(bang[i-1][j], bang[i][j-1], bang[i-1][j-1])
print("Số thao tác tối thiểu cần thực hiện:", bang[m][n])
#5.10
du_lieu = input("Nhập dữ liệu: ")
ket_qua = du_lieu.replace(" ", "")
print("Sau khi xóa khoảng trắng:", ket_qua)