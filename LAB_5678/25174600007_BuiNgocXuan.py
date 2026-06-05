
""" LAB 5: XỬ LÝ CHUỖI KÝ TỰ (STRING) """

#Bài 5.1: Nhập một số nguyên dương hệ thập phân và chuyển đổi nó sang dạng biểu diễn nhị phân.

n = int(input("Nhập số nguyên dương hệ thập phân: "))
nhi_phan = ""

while n > 0:
    nhi_phan = str(n % 2) + nhi_phan
    n = n // 2

print("Chuyển đổi sang dạng biểu diễn nhị phân là: ", nhi_phan)



#Bài 5.2: Nhập hai chuỗi ký tự str1 và str2, tìm và trích xuất chuỗi ký tự con chung có độ dài ngắn nhất giữa hai chuỗi.

str1 = input("Nhập chuỗi str1: ")
str2 = input("Nhập chuỗi str2: ")

ket_qua = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]

        if chuoi_con in str2:
            if ket_qua == "" or len(chuoi_con) < len(ket_qua):
                ket_qua = chuoi_con

if ket_qua != "":
    print("Chuỗi ký tự con chung có độ dài ngắn nhất giữa 2 chuỗi là: ", ket_qua)
else:
    print("Không tồn tại chuỗi ký tự con chung!")



#Bài 5.3: Tìm kiếm và thống kê tần suất: Nhập một chuỗi văn bản và một từ khóa. Hiển thị vị trí xuất hiện của từ khóa, đồng thời xác định và in ra từ xuất hiện với tần suất cao nhất trong chuỗi.    

van_ban = input("Nhập chuỗi văn bản: ")
tu_khoa = input("Nhập từ khóa cần tìm: ")
tu = van_ban.split()
vi_tri = []

for i in range(len(tu)):
    if tu[i] == tu_khoa:
        vi_tri.append(i)

if len(vi_tri) > 0:
    print("Vị trí xuất hiện của từ khóa: ", vi_tri)
else:
    print("Từ khóa không tồn tại!")

tan_suat = {}

for word in tu:
    if word in tan_suat:
        tan_suat[word] += 1
    else:
        tan_suat[word] = 1

tu_xh_max = ""
dem_max = 0

for word, dem in tan_suat.items():
    if dem > dem_max:
        dem_max = dem
        tu_xh_max = word

print("Từ xuất hiện với tần suất cao nhất trong chuỗi là: ", tu_xh_max)
print("Tần suất xuất hiện: ", dem_max)


#Bài 5.4: Loại bỏ tất cả các ký tự không phải là chữ số khỏi xâu. Chuyển đổi xâu kết quả thành số nguyên và kiểm tra tính nguyên tố.

import math

chuoi = input("Nhập chuỗi: ")
chu_so = ""

for ch in chuoi:
    if ch.isdigit():
        chu_so += ch

if chu_so == "":
    print("Chuỗi không tồn tại chữ số!")
else:
    so = int(chu_so)
    print("Số sau khi loại bỏ ký tự: ", so)

# Kiểm tra số nguyên tố
    if so < 2:
        print(so, "Không phải số nguyên tố!")
    else:
        là_so_ngto = True

        for i in range(2, int(math.sqrt(so)) + 1):
            if so % i == 0:
                la_so_ngto = False
                break

        if la_so_ngto:
            print(so, "là số nguyên tố")
        else:
            print(so, "Không là số nguyên tố!")


# Bài 5.5: Trộn hai chuỗi ký tự bằng cách lấy lần lượt từng ký tự từ trái sang phải của mỗi chuỗi, phân tách nhau bởi dấu gạch nối -.    

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
kq = ""

max_len = max(len(str1), len(str2))

# Trộn ký tự hai chuỗi
for i in range(max_len):

    if i < len(str1):
        kq += str1[i]

    kq += "-"

    if i < len(str2):
        kq += str2[i]

# Không thêm dấu "-" ở cuối
    if i != max_len - 1:
        kq += "-"

print("Chuỗi sau khi trộn các ký tự: ", kq)    


# Bài 5.6: Đếm số lần xuất hiện của từng ký tự đặc biệt không thuộc nhóm chữ cái hoặc chữ số. Tính toán tỷ lệ phần trăm của mỗi ký tự đặc biệt trên tổng độ dài xâu.

chuoi = input("Nhập chuỗi: ")
kytu_dac_biet = {}

# Đếm ký tự đặc biệt
for ch in chuoi:
    if not ch.isalnum() and not ch.isspace():
        if ch in kytu_dac_biet:
            kytu_dac_biet[ch] += 1
        else:
            kytu_dac_biet[ch] = 1

do_dai = len(chuoi)

print("Kết quả sau thống kê: ")

for ch, dem in kytu_dac_biet.items():
    phan_tram = (dem / do_dai) * 100
    print(f"Ký tự '{ch}' xuất hiện {dem} lần, chiếm {phan_tram:.2f}% tổng độ dài xâu!")


# Bài 5.7: Thống kê chi tiết số lượng chữ cái in thường, in hoa, chữ số và ký tự đặc biệt xuất hiện trong một xâu cho trước.

chuoi = input("Nhập chuỗi: ")
in_thuong = 0
in_hoa = 0
so = 0
kytu_dac_biet = 0

for ch in chuoi:
    if ch.islower():
        in_thuong += 1
    elif ch.isupper():
        in_hoa += 1
    elif ch.isdigit():
        so += 1
    elif not ch.isspace():
        kytu_dac_biet += 1

print("KẾT QUẢ SAU THỐNG KÊ")
print("Số chữ cái in thường: ", in_thuong)
print("Số chữ cái in hoa: ", in_hoa)
print("Số chữ số: ", so)
print("Số ký tự đặc biệt: ", kytu_dac_biet)


# Bài 5.8: Áp dụng trên xâu có độ dài lớn hơn 10 ký tự: trích xuất xâu con từ vị trí 2 đến 8, trích xuất 5 ký tự từ vị trí 5, lấy 3 ký tự cuối cùng, chuyển đổi toàn bộ sang định dạng chữ hoa/chữ thường và đảo ngược xâu.

chuoi = input("Nhập xâu (chuỗi): ")
if len(chuoi) > 10:

    # Xâu con từ vị trí 2 đến 8
    xau1 = chuoi[2:9]

    # Lấy 5 ký tự từ vị trí 5
    xau2 = chuoi[5:10]

    # Lấy 3 ký tự cuối
    xau3 = chuoi[-3:]

    chu_hoa = chuoi.upper()
    chu_thuong = chuoi.lower()
    dao_nguoc = chuoi[::-1]

    print("KẾT QUẢ")
    print("Xâu con từ vị trí 2 đến 8: ", xau1)
    print("5 ký tự từ vị trí 5: ", xau2)
    print("3 ký tự cuối: ", xau3)
    print("Chuyển đổi sang chữ hoa: ", chu_hoa)
    print("Chuyển đổi sang chữ thường: ", chu_thuong)
    print("Đảo ngược xâu: ", dao_nguoc)
else:
    print("Xâu phải có độ dài lớn hơn 10 ký tự!")


# Bài 5.9: Đánh giá khả năng chuyển đổi chuỗi ban đầu thành một chuỗi mục tiêu thông qua các thao tác thêm, xóa hoặc thay thế ký tự.

s1 = input("Nhập chuỗi ban đầu: ")
s2 = input("Nhập chuỗi mục tiêu: ")

# Tính khoảng cách chuyển đổi giữa 2 chuỗi
m = len(s1)
n = len(s2)

# Tạo ma trận lưu kết quả
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Khởi tạo hàng và cột đầu tiên
for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

# Tính số thao tác tối thiểu
for i in range(1, m + 1):
    for j in range(1, n + 1):

        # Nếu ký tự giống nhau
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        # Nếu khác nhau
        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],     # Xóa
                dp[i][j - 1],     # Thêm
                dp[i - 1][j - 1]  # Thay thế
            )
print("Số thao tác tối thiểu cần thực hiện: ", dp[m][n])


# Bài 5.10: Xử lý và loại bỏ toàn bộ các ký tự khoảng trắng xuất hiện bên trong một xâu dữ liệu.

xau = input("Nhập xâu: ")
khoang_trang = xau.replace(" ", "")

print("Xâu sau khi loại bỏ toàn bộ ký tự khoảng trắng: ")
print(khoang_trang)






""" LAB 6: DANH SÁCH VÀ BỘ (LIST & TUPLE) """

# Bài 6.1: Nhập mảng gồm n số nguyên dương. Tiến hành phân loại và tính tổng độc lập cho nhóm các số chẵn và nhóm các số lẻ.

n = int(input("Nhập n số nguyên dương: "))
mang = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    mang.append(x)

# Khởi tạo biến tổng
tong_chan = 0
tong_le = 0

for so in mang:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

print("Mảng đã nhập: ", mang)
print("Tổng độc lập của các số chẵn: ", tong_chan)
print("Tổng độc lập của các số lẻ: ", tong_le)


# Bài 6.2: Khảo sát mảng n số nguyên dương đầu vào. Trích xuất và xuất ra màn hình toàn bộ các phần tử thỏa mãn điều kiện là số nguyên tố hoặc số hoàn hảo.

def la_so_ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def la_so_hoan_hao(n):
    if n < 2:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

n = int(input("Nhập n số nguyên dương: "))
mang = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    mang.append(x)

kq = []

for so in mang:
    if la_so_ngto(so) or la_so_hoan_hao(so):
        kq.append(so)

print("Các phần tử là số nguyên tố hoặc số hoàn hảo: ")
print(kq)


# Bài 6.3: Tiếp nhận một dãy số hỗn hợp gồm các số nguyên và số thực. Tìm kiếm và in ra giá trị lớn nhất cũng như giá trị nhỏ nhất tồn tại trong dãy.

n = int(input("Nhập dãy số hỗn hợp: "))
day_so = []

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    day_so.append(x)

gia_tri_max = max(day_so)
gia_tri_min = min(day_so)

print("Dãy số: ", day_so)
print("Giá trị lớn nhất: ", gia_tri_max)
print("Giá trị nhỏ nhất: ", gia_tri_min)


# Bài 6.4: Vận dụng kỹ thuật List Comprehension để khởi tạo và lưu trữ danh sách gồm n số hạng đầu tiên thuộc dãy số Fibonacci.

n = int(input("Nhập n số phần tử: "))
fib = [0, 1]

# Sinh thêm các số Fibonacci
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
# Lấy đúng n phần tử đầu tiên
fib = fib[:n]

print("Dãy Fibonacci: ", fib)


# Bài 6.5: Ứng dụng cú pháp List Comprehension để thiết lập một danh sách chứa toàn bộ các số nguyên tố có giá trị nhỏ hơn 100.

def la_so_ngto(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sử dụng List Comprehension
ngto_list = [x for x in range(100) if la_so_ngto(x)]

print("Các số nguyên tố có giá trị nhỏ hơn 100: ")
print(ngto_list)


# Bài 6.6: Khảo sát một dãy số nguyên đầu vào. Thực hiện tính toán sai phân giữa các phần tử liên tiếp để đối chiếu và kết luận dãy số có cấu thành một cấp số cộng hay không.

n = int(input("Nhập số lượng phần tử: "))
day_so = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    day_so.append(x)

cap_so_cong = True
cong_sai = day_so[1] - day_so[0]

for i in range(1, n - 1):
    if day_so[i + 1] - day_so[i] != cong_sai:
        cap_so_cong = False
        break

print("Dãy số: ", day_so)

if cap_so_cong:
    print("Đây là cấp số cộng.")
    print("Công sai là: ", cong_sai)
else:
    print("Dãy số không phải là cấp số cộng!")


# Bài 6.7: Tiếp nhận dữ liệu cấu thành ma trận kích thước m × n từ người dùng. Thực hiện tính toán tổng của toàn bộ các phần tử bên trong ma trận đó.

m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
tong = 0

for i in range(m):
    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        tong += x

print("Tổng các phần tử trong ma trận là: ", tong)


# Bài 6.8: Thiết lập cấu trúc lưu trữ cho hai ma trận riêng biệt, kiểm tra điều kiện nhân và lập trình thuật toán tính tích của hai ma trận.

m = int(input("Nhập số hàng của ma trận A: "))
n = int(input("Nhập số cột của ma trận A: "))
A = []

print("Nhập các phần tử của ma trận A: ")
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(int(input(f"A[{i}][{j}] = ")))
    A.append(hang)

m2 = int(input("Nhập số hàng của ma trận B: "))
n2 = int(input("Nhập số cột của ma trận B: "))

if n != m2:
    print("Hai ma trận không thể nhân với nhau!")
else:
    B = []
    print("Nhập các phần tử của ma trận B: ")
    for i in range(m2):
        hang = []
        for j in range(n2):
            hang.append(int(input(f"B[{i}][{j}] = ")))
        B.append(hang)

# ma trận kết quả C
    C = []
    for i in range(m):
        hang = []
        for j in range(n2):
            hang.append(0)
        C.append(hang)

# Tính tích ma trận
    for i in range(m):
        for j in range(n2):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    print("Ma trận tích C = A x B: ")
    for hang in C:
        print(hang)


# Bài 6.9: Xây dựng ma trận chuyển vị bằng cách hoán đổi hàng và cột của ma trận gốc. Ứng dụng kết quả này để kiểm tra tính đối xứng của một ma trận vuông.

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
# ma trận
A = []
print("Nhập các phần tử của ma trận A: ")

for i in range(m):
    hang = []
    for j in range(n):
        hang.append(int(input(f"A[{i}][{j}] = ")))
    A.append(hang)

# Tạo ma trận chuyển vị
AT = []
for j in range(n):
    hang = []
    for i in range(m):
        hang.append(A[i][j])
    AT.append(hang)

print("Ma trận chuyển vị: ")
for hang in AT:
    print(hang)

# Kiểm tra đối xứng
if m != n:
    print("Đây không phải ma trận vuông nên không thể là ma trận đối xứng!")
else:
    doi_xung = True

    for i in range(m):
        for j in range(n):
            if A[i][j] != AT[i][j]:
                doi_xung = False
                break
        if not doi_xung:
            break

    if doi_xung:
        print("Ma trận là ma trận đối xứng.")
    else:
        print("Ma trận không đối xứng!")    


# Bài 6.10: Phát triển thuật toán tìm kiếm và xuất ra màn hình ma trận nghịch đảo của một ma trận vuông cấp n, với điều kiện ma trận đó khả nghịch.

import numpy as np

n = int(input("Nhập cấp n của ma trận vuông: "))
A = []
print("Nhập các phần tử của ma trận: ")

for i in range(n):
    hang = list(map(float, input(f"Hàng {i + 1}: ").split()))
    A.append(hang)

A = np.array(A)

# Tính định thức
det = np.linalg.det(A)

if abs(det) < 1e-10:
    print("Ma trận không khả nghịch (định thức bằng 0)!")
else:
    A_inv = np.linalg.inv(A)

    print("Ma trận nghịch đảo:")
    print(A_inv)




""" LAB 7: TẬP HỢP VÀ TỪ ĐIỂN (SET & DICTIONARY) """

# Bài 7.1: Nhập số nguyên N, khởi tạo một từ điển có kích thước N với khóa là x và giá trị tương ứng được tính bằng x3.

N = int(input("Nhập N: "))
dic = {}

for x in range(1, N + 1):
    dic[x] = x ** 3

print(dic)


# Bài 7.2: Xây dựng từ điển lưu trữ thông tin tên và điểm thi của sinh viên. Thực hiện thuật toán ánh xạ điểm số sang các mức xếp loại học thuật chuẩn từ A đến F.

n = int(input("Nhập số lượng sinh viên: "))
sinh_vien = {}

for i in range(n):
    ten = input(f"Nhập tên sinh viên {i + 1}: ")
    diem = float(input("Nhập điểm: "))
    sinh_vien[ten] = diem

def xep_loai(diem):
    if diem >= 90:
        return 'A'
    elif diem >= 80:
        return 'B'
    elif diem >= 70:
        return 'C'
    elif diem >= 60:
        return 'D'
    elif diem >= 50:
        return 'E'
    else:
        return 'F'

print("Kết quả xếp loại: ")
for ten, diem in sinh_vien.items():
    print(f"{ten}: {diem} điểm - Xếp loại {xep_loai(diem)}")


# Bài 7.3: Dựa trên từ điển dữ liệu sinh viên đã phân loại, thiết lập một từ điển đếm tần suất để báo cáo số lượng sinh viên đạt được ở từng mức học lực.

sinh_vien = {
    "An": "A",
    "Hiếu": "B",
    "Cường": "A",
    "Dung": "C",
    "Linh": "B",
    "Long": "A"
}
tan_suat = {}

for hoc_luc in sinh_vien.values():
    if hoc_luc in tan_suat:
        tan_suat[hoc_luc] += 1
    else:
        tan_suat[hoc_luc] = 1

print("Thống kê số lượng sinh viên theo mức học lực: ")
for hoc_luc, so_luong in tan_suat.items():
    print(f"Học lực {hoc_luc}: {so_luong} sinh viên")


# Bài 7.4: Khảo sát một đoạn văn bản tiếng Anh. Xử lý làm sạch chuỗi và sử dụng cấu trúc từ điển để lưu trữ số lần xuất hiện của từng từ vựng riêng biệt.

van_ban = input("Nhập đoạn văn bản tiếng Anh: ")
van_ban = van_ban.lower()

# Loại bỏ dấu câu
for ky_tu in ",.;:!?()[]{}\"'":
    van_ban = van_ban.replace(ky_tu, "")

danh_sach_tu = van_ban.split()
tan_suat = {}

for tu in danh_sach_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

print("Số lần xuất hiện của từng từ vựng: ")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")


# Bài 7.5: Tiếp nối dữ liệu từ điển ở bài phân tích văn bản, xây dựng thuật toán duyệt để tìm kiếm và xuất ra các từ có tần suất xuất hiện cao nhất và thấp nhất.

max_ts = max(tan_suat.values())
min_ts = min(tan_suat.values())

# từ có tần suất lớn nhất
tu_max = []
for tu, ts in tan_suat.items():
    if ts == max_ts:
        tu_max.append(tu)

# từ có tần suất nhỏ nhất
tu_min = []
for tu, ts in tan_suat.items():
    if ts == min_ts:
        tu_min.append(tu)

print("Các từ có tần suất xuất hiện cao nhất: ")
for tu in tu_max:
    print(f"{tu}: {max_ts} lần")

print("Các từ có tần suất xuất hiện thấp nhất: ")
for tu in tu_min:
    print(f"{tu}: {min_ts} lần")


# Bài 7.6: Thao tác trên từ điển quản lý hành trang (Inventory). Bổ sung trường dữ liệu mới (khóa pocket chứa danh sách vật phẩm) và cập nhật số lượng cho khóa gold.  

# Từ điển ban đầu
inventory = {
    "gold": 500,
    "rope": 1,
    "torch": 6,
    "arrow": 12
}
# Thêm khóa pocket
inventory["pocket"] = ["now", "apple"]

# Cập nhật số cho khóa gold
inventory["gold"] = 750

print("Thông tin hành trang sau khi cập nhật: ")
for khoa, gia_tri in inventory.items():
    print(khoa, ":", gia_tri)  


# Bài 7.7: Thực hiện sắp xếp theo thứ tự từ điển cho danh sách các vật phẩm nằm trong khóa backpack và loại bỏ một vật phẩm cụ thể khỏi danh sách này.

inventory = {
    "gold": 500,
    "backpack": ["rope", "apple", "torch", "dagger", "bread"]
}

# Sắp xếp theo thứ tự từ điển
inventory["backpack"].sort()

# Xóa vật phẩm torch
if "torch" in inventory["backpack"]:
    inventory["backpack"].remove("torch")

print("Danh sách vật phẩm trong backpack: ")
print(inventory["backpack"])


# Bài 7.8: Vận dụng hai từ điển biểu diễn thông tin số lượng tồn kho và đơn giá. Tính toán chi phí, định dạng và in hóa đơn chi tiết cho các mặt hàng.

so_luong = {
    "Bút bi": 10,
    "Vở": 10,
    "Thước": 10,
    "Tẩy": 5
}
don_gia = {
    "Bút bi": 5000,
    "Vở": 10000,
    "Thước": 8000,
    "Tẩy": 5000
}
tong_tien = 0

print("-" * 50)
print("{:<15}{:>10}{:>12}{:>13}".format(
    "Mặt hàng", "Số lượng", "Đơn giá", "Thành tiền"))
print("-" * 50)

for mat_hang in so_luong:
    sl = so_luong[mat_hang]
    gia = don_gia[mat_hang]
    thanh_tien = sl * gia
    tong_tien += thanh_tien

    print("{:<15}{:>10}{:>12,}{:>13,}".format(
        mat_hang, sl, gia, thanh_tien))

print("-" * 50)
print("{:<37}{:>13,}".format("Tổng cộng: ", tong_tien))


# Bài 7.9: Phát triển thủ tục khấu trừ số lượng vật phẩm đã giao dịch thành công và xuất ra báo cáo tình trạng số lượng tồn kho cập nhật của cửa hàng

ton_kho = {
    "Bút bi": 40,
    "Vở": 20,
    "Thước": 10,
    "Tẩy": 5
}
giao_dich = {
    "Bút bi": 10,
    "Vở": 10,
    "Tẩy": 5
}

for mat_hang, so_luong_mua in giao_dich.items():
    if mat_hang in ton_kho and ton_kho[mat_hang] >= so_luong_mua:
        ton_kho[mat_hang] -= so_luong_mua

print("Cập nhật số lượng tồn kho của cửa hàng: ")
for mat_hang, so_luong in ton_kho.items():
    print(mat_hang, ":", so_luong)


# Bài 7.10: Vận dụng cấu trúc Set để biểu diễn danh mục sản phẩm của kho hàng. Sử dụng phép toán tập hợp để trích xuất các mặt hàng có trong kho nhưng chưa được khách hàng chọn mua.

kho_hang = {
    "Bút bi",
    "Vở",
    "Thước",
    "Tẩy",
    "Compa"
}
khach_mua = {
    "Bút bi",
    "Vở",
    "Tẩy"
}
chua_mua = kho_hang - khach_mua

print("Các mặt hàng chưa được khách chọn mua: ")
for mat_hang in chua_mua:
    print("-", mat_hang)




""" LAB 8: XÂY DỰNG HÀM TÙY BIẾN """

# Bài 8.1: Xây dựng hàm kiểm tra số nguyên tố độc lập. Ứng dụng hàm này để quét, tìm kiếm và xuất ra toàn bộ các cặp số nguyên tố sinh đôi có giá trị nhỏ hơn 1000.

import math

def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Các cặp số nguyên tố sinh đôi có giá trị nhỏ hơn 1000: ")

for n in range(2, 999):
    if la_so_nguyen_to(n) and la_so_nguyen_to(n + 2):
        print(f"({n}, {n + 2})")


# Bài 8.2: Khai báo hàm xử lý toán học để tính giai thừa của một số nguyên dương, tạo tiền đề nền tảng cho các bài toán phân tích tổ hợp phức tạp.

def giai_thua(n):
    if n < 0:
        return None
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

n = int(input("Nhập số nguyên dương n: "))
print(f"{n}! = {giai_thua(n)}")


# Bài 8.3: Kế thừa hàm giai thừa vừa xây dựng, phát triển cấu trúc hàm tính số hoán vị của n phần tử chập r và số tổ hợp của n phần tử chập r.

def giai_thua(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

def hoan_vi(n, r):
    if r > n or r < 0:
        return 0
    return giai_thua(n) // giai_thua(n - r)

def to_hop(n, r):
    if r > n or r < 0:
        return 0
    return giai_thua(n) // (giai_thua(r) * giai_thua(n - r))

n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

print("Số hoán vị P(n,r) = ", hoan_vi(n, r))
print("Số tổ hợp C(n,r) = ", to_hop(n, r))


# Bài 8.4: Thiết lập hàm cubesum nhận tham số đầu vào là một số nguyên, thực hiện bóc tách và trả về tổng các lập phương từ các chữ số cấu thành số đó.

def cubesum(n):
    tong = 0

    while n > 0:
        chu_so = n % 10
        tong += chu_so ** 3
        n //= 10
    return tong

n = int(input("Nhập một số nguyên: "))
print("Tổng lập phương các chữ số = ", cubesum(n))


# Bài 8.5: Khai thác lại hàm cubesum để xây dựng hàm logic isArmstrong nhằm đánh giá tính chất Armstrong của một số, đồng thời viết thủ tục xuất danh sách các số này.

def cubesum(n):
    tong = 0
    tam_thoi = n

    while tam_thoi > 0:
        chu_so = tam_thoi % 10
        tong += chu_so ** 3
        tam_thoi //= 10
    return tong

def isArmstrong(n):
    return n == cubesum(n)

def liet_ke_armstrong():
    print("Các số Armstrong nhỏ hơn 1000: ")

    for i in range(1, 1000):
        if isArmstrong(i):
            print(i, end=" ")

liet_ke_armstrong()


# Bài 8.6: Phát triển thuật toán và đóng gói thành hàm sumPdivisors chịu trách nhiệm tìm kiếm và tính tổng tất cả các ước số thực sự của một số nguyên dương đầu vào.

def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

n = int(input("Nhập số nguyên dương n: "))
print("Tổng các ước số thực sự của", n, "là:", sumPdivisors(n))


# Bài 8.7: Ứng dụng hàm sumPdivisors để thiết lập hàm kiểm tra xem hai số nguyên độc lập có cấu thành một cặp số Amicable hay không theo định nghĩa toán học.

def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

if isAmicable(a, b):
    print(a, "và", b, "là một cặp số Amicable.")
else:
    print(a, "và", b, "không phải là một cặp số Amicable!")


# Bài 8.8: Vận dụng hàm filter kết hợp cùng cú pháp lambda để phân tách một cách độc lập nhóm số chẵn và nhóm số lẻ từ một mảng dữ liệu hỗn hợp.

ds = [12, 5, 8, 17, 20, 33, 42, 7, 14, 25]

so_chan = list(filter(lambda x: x % 2 == 0, ds))
so_le = list(filter(lambda x: x % 2 != 0, ds))

print("nhóm danh sách dữ liệu ban đầu: ", ds)
print("Các số chẵn: ", so_chan)
print("Các số lẻ: ", so_le)


# Bài 8.9: Triển khai hàm map để xử lý dữ liệu hàng loạt, khởi tạo danh sách mới chứa giá trị lập phương của toàn bộ các phần tử thuộc mảng gốc.

ds = [1, 2, 3, 4, 5]
lap_phuong = list(map(lambda x: x ** 3, ds))

print("Danh sách gốc: ", ds)
print("Danh sách mới chứa giá trị lập phương: ", lap_phuong)


# Bài 8.10: Phối hợp đồng thời hai kỹ thuật map và filter để thiết lập một đường ống xử lý dữ liệu: tính lập phương riêng cho tập hợp số chẵn và bình phương riêng cho tập hợp số lẻ.

ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lap_phuong_chan = list(
    map(lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, ds))
)
binh_phuong_le = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, ds))
)

print("Danh sách gốc: ", ds)
print("Lập phương  cho tập hợp các số chẵn: ", lap_phuong_chan)
print("Bình phương cho tập hợp các số lẻ: ", binh_phuong_le)













