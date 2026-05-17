# Bài 5.1: Nhập một số nguyên dương hệ thập phân và chuyển đổi nó sang dạng biểu diễn nhị phân
n = int(input("Nhập n: "))
nhi_phan = ""

while n > 0:
    nhi_phan = str(n % 2) + nhi_phan
    n //= 2
print(f"{n} biểu diễn dạng nhị phân là: {nhi_phan}")
 

# Bài 5.2: Nhập hai chuỗi ký tự str1 và str2, tìm và trích xuất chuỗi ký tự con chung có độ dài ngắn nhất giữa hai chuỗi
str1 = input("Nhập chuỗi ký tự str1: ")
str2 = input("Nhập chuỗi ký tự str2: ")

chung = ""
for do_dai in range(1, min(len(str1), len(str2))+1):
    found = False
    for i in range(len(str1) - do_dai+1):
        sub = str1[i : i + do_dai]

        if sub in str2:
            found = True
            break
    if found: 
        break

if chung != "":
    print("Chuỗi con chung ngắn nhất là:", chung)
else:
    print("Không có chuỗi con chung")

# Bài 5.3: Tìm kiếm và thống kê tần suất: Nhập một chuỗi văn bản và một từ khóa. Hiển
# thị vị trí xuất hiện của từ khóa, đồng thời xác định và in ra từ xuất hiện với tần suất
# cao nhất trong chuỗi
chuoi = input("Nhập vào chuỗi: ")
tu_khoa = input("Nhập từ khóa: ")
ds_tu = chuoi.split()

vi_tri = []
for i in range(len(ds_tu)):
    if ds_tu[i] == tu_khoa:
        vi_tri.append(i)

if len(vi_tri) > 0:
    print("Vị trí của từ khóa là:")
    for v in vi_tri:
        print(v)

else:
    print("Không có từ khóa trong chuỗi")

tu_nhieu_nhat = ""
so_lan_nhieu_nhat = 0

for tu in ds_tu:
    so_lan = ds_tu.count(tu)
    if so_lan > so_lan_nhieu_nhat:
        so_lan_nhieu_nhat = so_lan
        tu_nhieu_nhat = tu

print("Từ xuất hiện nhiều nhất là:", tu_nhieu_nhat)
print("Số lần xuất hiện là:", so_lan_nhieu_nhat)


# Bài 5.4: Loại bỏ tất cả các ký tự không phải là chữ số khỏi xâu. Chuyển đổi xâu kết quả thành số nguyên và kiểm tra tính nguyên tố
chuoi = input("Nhập chuỗi: ")
chuoi_so = ""
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chuoi_so += ky_tu

if chuoi_so == "":
    print("Không có ký tự trong chuỗi")
else:
    so = int(chuoi_so)
    print("Số sau khi loại bỏ ký tự là:", so)

if so < 2:
    print("Không là số nguyên tố")
else: 
    la_ngto = True
    for i in range(2, so):
        if so % i == 0:
            la_ngto = False
            break

if la_ngto:
    print("Là số nguyên tố")
else:
    print("Không là số nguyên tố")


# Bài 5.5: Trộn hai chuỗi ký tự bằng cách lấy lần lượt từng ký tự từ trái sang phải của mỗi chuỗi, phân tách nhau bởi dấu gạch nối
chuoi1 = input("Nhập chuỗi 1: ")
chuoi2 = input("Nhập chuỗi 2: ")
ket_qua = ""
do_dai_nho = min(len(chuoi1), len(chuoi2))

for i in range(do_dai_nho):
    ket_qua += chuoi1[i]
    ket_qua += "-"
    ket_qua += chuoi2[i]

    if i != do_dai_nho - 1:
        ket_qua += "-"

print("Chuỗi sau khi trộn là: ")
print(ket_qua)


# Bài 5.6: Đếm số lần xuất hiện của từng ký tự đặc biệt không thuộc nhóm chữ cái hoặc chữ số. 
# Tính toán tỷ lệ phần trăm của mỗi ký tự đặc biệt trên tổng độ dài xâu
chuoi = input("Nhập chuỗi: ")
tong_do_dai = len(chuoi)
da_dem = []
for ky_tu in chuoi:
    if not ky_tu.isalpha() and not ky_tu.isdigit() and ky_tu != " ":
        if ky_tu not in da_dem:
            
            so_lan = chuoi.count(ky_tu)

            ty_le = (so_lan / tong_do_dai) * 100

            print("Ký tự đặc biệt:", ky_tu)
            print("Số lần xuất hiện:", so_lan)
            print("Tỷ lệ phần trăm:", round(ty_le, 2), "%")
            print()

            da_dem.append(ky_tu)


# Bài 5.7: Thống kê chi tiết số lượng chữ cái in thường, in hoa, chữ số và ký tự đặc biệt xuất hiện trong một xâu cho trước
xau = input("Nhập xâu: ")

thuong = 0
hoa = 0
so = 0
dac_biet = 0

for ky_tu in xau:
    if ky_tu.islower():
        thuong += 1
    elif ky_tu.isupper():
        hoa += 1
    elif ky_tu.isdigit():
        so += 1
    else:
        dac_biet += 1

print("Số lượng chữ cái in thường là:", thuong)
print("Số lượng chữ cái in hoa là:", hoa)
print("Số lượng chữ số là:", so)
print("Số lượng ký tự đặc biệt là:", dac_biet)


# Bài 5.8: Áp dụng trên xâu có độ dài lớn hơn 10 ký tự: trích xuất xâu con từ vị trí 2 đến 8, 
# trích xuất 5 ký tự từ vị trí 5, lấy 3 ký tự cuối cùng, chuyển đổi toàn bộ sang định
# dạng chữ hoa/chữ thường và đảo ngược xâu
xau = input("Nhập xâu: ")
if len(xau) > 10:
    print("Xâu con từ vị trí 2 đến 8:", xau[2:9])
    print("5 ký tự tự vị trí 5:", xau[5:10])
    print("3 ký tự cuối cùng:", xau[-3:])
    print("Định dạng chữ hoa:", xau.upper())
    print("Định dạng chữ thường:", xau.lower())
    print("Đảo ngược xâu:", xau[::-1])


# Bài 5.9: Đánh giá khả năng chuyển đổi chuỗi ban đầu thành một chuỗi mục tiêu thông qua các thao tác thêm, xóa hoặc thay thế ký tự
s1 = input("Nhập chuỗi ban đầu: ")
s2 = input("Nhập chuỗi mục tiêu: ")

if s1 == s2:
    print("2 chuỗi đã giống nhau")
else:
    print("Có thể chuyển đổi chuỗi thông qua các thao tác:")

    min_len = min(len(s1), len(s2))

    for i in range(min_len):
        if s1[i] != s2[i]:
            print(f"Thay ký tự {s1[i]} bằng ký tự {s2[i]} tại vị trí {i}")

    if len(s1) < len(s2):
        for i in range(len(s1), len(s2)):
            print(f"Thêm ký tự {s2[i]} vào vị trí {i}")

    if len(s1) > len(s2):
        for i in range(len(s2), len(s1)):
            print(f"Xóa ký tự {s1[i]} tịa vị trí {i}")
            

# Bài 5.10: Xử lý và loại bỏ toàn bộ các ký tự khoảng trắng xuất hiện bên trong một xâu dữ liệu
xau = input("Nhập xâu: ")
kq = xau.replace(" ", "")
print("Sau khi xử lý và loại bỏ toàn bộ khoảng trắng xuất hiện bên trong xâu:", kq)

