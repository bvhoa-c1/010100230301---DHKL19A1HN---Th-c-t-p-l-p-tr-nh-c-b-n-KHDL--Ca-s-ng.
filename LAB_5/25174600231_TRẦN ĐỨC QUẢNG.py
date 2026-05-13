"""LAB5 : XỬ LÝ CHUỖI KÝ TỰ """

# bài 5.1 
n = float(input("nhập số nguyên dương: "))
result = ""
temp = n
while temp > 0 :
    result = str(temp % 2) + result
    temp = temp // 2
print("nhi phan : ", result)

# bai 5.2
str1 = input("nhập str1 : ")
str2 = input("nhập str2: ")
shortly = ""
for i in range(len(str1)):
    for j in range(i + 1, len(str1)+1):
        sub = str1[i:j]
        if sub in str2 : 
            if shortly == "" or len(sub) < len(shortly) :
                shortly = sub
print("chuỗi con chung ngắn nhất: ", shortly)

# bài 5.3 :
van_ban = input("Nhập chuỗi: ")
tu_khoa = input("Nhập từ cần tìm: ")

vi_tri = van_ban.find(tu_khoa)
print(f"Vị trí đầu tiên của '{tu_khoa}' là: {vi_tri}")

danh_sach_tu = van_ban.split() 
tu_nhieu_nhat = max(danh_sach_tu, key=van_ban.count)
print("Từ xuất hiện nhiều nhất là:", tu_nhieu_nhat)


# bài 5.4
xau = input("Nhập xâu: ")
so_da_loc = ""

for ky_tu in xau:
    if ky_tu.isdigit():
        so_da_loc = so_da_loc + ky_tu

n = int(so_da_loc)
la_so_nguyen_to = True
for i in range(2, n):
    if n % i == 0:
        la_so_nguyen_to = False
        break

print(f"Số sau khi lọc: {n}. Là số nguyên tố: {la_so_nguyen_to}")


# bài 5.5
s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")
ket_qua = ""

do_dai = min(len(s1), len(s2))

for i in range(do_dai):
    ket_qua += s1[i] + "-" + s2[i]
    if i < do_dai - 1:
        ket_qua += "-"

print("Kết quả trộn:", ket_qua)

# bài 5.6
s = input("Nhập xâu: ")
tong_ky_tu = len(s)
hoa = thuong = so = dac_biet = 0

for k in s:
    if k.isupper(): hoa += 1
    elif k.islower(): thuong += 1
    elif k.isdigit(): so += 1
    else: dac_biet += 1

print(f"Hoa: {hoa}, Thường: {thuong}, Số: {so}, Đặc biệt: {dac_biet}")
if tong_ky_tu > 0:
    print(f"Tỷ lệ ký tự đặc biệt: {(dac_biet/tong_ky_tu)*100}%")


# bài 5.7
s = input("Nhập xâu (>10 ký tự): ")
if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[2:9])
    print("5 ký tự từ vị trí 5:", s[5:10])
    print("3 ký tự cuối:", s[-3:])
    print("Viết hoa:", s.upper())
    print("Viết thường:", s.lower())
    print("Đảo ngược:", s[::-1])


# bài 5.8 :
s_goc = input("Chuỗi gốc: ")
s_dich = input("Chuỗi đích: ")


buoc_thay_the = 0
min_len = min(len(s_goc), len(s_dich))

for i in range(min_len):
    if s_goc[i] != s_dich[i]:
        buoc_thay_the += 1

chen_xoa = abs(len(s_goc) - len(s_dich))
print(f"Ước lượng cần ít nhất {buoc_thay_the + chen_xoa} thao tác.")

# bài 5.9 :
s_goc = input("Chuỗi gốc: ")
s_dich = input("Chuỗi đích: ")

buoc_thay_the = 0
min_len = min(len(s_goc), len(s_dich))

for i in range(min_len):
    if s_goc[i] != s_dich[i]:
        buoc_thay_the += 1

chen_xoa = abs(len(s_goc) - len(s_dich))
print(f"Ước lượng cần ít nhất {buoc_thay_the + chen_xoa} thao tác.")


# bài 5.10 :
xau = input("Nhập xâu có khoảng trắng: ")
print("Kết quả:", xau.replace(" ", ""))