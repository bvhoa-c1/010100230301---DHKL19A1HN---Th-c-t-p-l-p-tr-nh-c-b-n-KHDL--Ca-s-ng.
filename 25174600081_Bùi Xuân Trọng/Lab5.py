# Bài 5.1
n = int(input("Nhập số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    nhi_phan = ""
    temp = n
    while temp > 0:
        nhi_phan = str(temp % 2) + nhi_phan
        temp //= 2
    print(f"Dạng biểu diễn nhị phân là: {nhi_phan}")
# Bài 5.2
str1 = input("Nhập chuỗi str1: ")
str2 = input("Nhập chuỗi str2: ")

chung = []
# Duyệt tìm tất cả chuỗi con của str1 có nằm trong str2
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2:
            chung.append(chuoi_con)

if chung:
    # Hàm min() với key=len sẽ tự động tìm chuỗi có độ dài ngắn nhất
    ngan_nhat = min(chung, key=len)
    print(f"Chuỗi con chung ngắn nhất là: '{ngan_nhat}'")
else:
    print("Hai chuỗi không có ký tự chung nào.")
# Bài 5.3
van_ban = input("Nhập chuỗi văn bản: ")
tu_khoa = input("Nhập từ khóa cần tìm: ")

# 1. Hiển thị vị trí từ khóa (dùng find() tìm nhiều lần)
vi_tri = []
idx = van_ban.find(tu_khoa)
while idx != -1:
    vi_tri.append(idx)
    idx = van_ban.find(tu_khoa, idx + 1)
print(f"Các vị trí xuất hiện của từ khóa '{tu_khoa}': {vi_tri}")

# 2. Tìm từ xuất hiện nhiều nhất (cắt theo khoảng trắng)
cac_tu = van_ban.split()
if cac_tu:
    tan_suat = {}
    for tu in cac_tu:
        tan_suat[tu] = tan_suat.get(tu, 0) + 1
        
    tu_max = max(tan_suat, key=tan_suat.get)
    print(f"Từ xuất hiện nhiều nhất là: '{tu_max}' (tần suất: {tan_suat[tu_max]} lần)")
# Bài 5.4
import math

s = input("Nhập xâu: ")
# Lọc ra chuỗi chỉ chứa số
chuoi_so = "".join([c for c in s if c.isdigit()])

if not chuoi_so:
    print("Xâu không chứa chữ số nào.")
else:
    n = int(chuoi_so)
    print(f"Số nguyên trích xuất được: {n}")
    
    # Kiểm tra nguyên tố
    if n < 2:
        print(f"{n} KHÔNG phải là số nguyên tố.")
    else:
        la_nguyen_to = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                la_nguyen_to = False
                break
        print(f"{n} {'LÀ' if la_nguyen_to else 'KHÔNG PHẢI là'} số nguyên tố.")
# Bài 5.5
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

ket_qua = []
do_dai_min = min(len(str1), len(str2))

# Trộn xen kẽ
for i in range(do_dai_min):
    ket_qua.append(str1[i])
    ket_qua.append(str2[i])

# Đưa phần thừa vào mảng (nếu có)
if len(str1) > do_dai_min: ket_qua.extend(list(str1[do_dai_min:]))
if len(str2) > do_dai_min: ket_qua.extend(list(str2[do_dai_min:]))

# Nối các phần tử bằng dấu gạch nối
print("Chuỗi sau khi trộn: " + "-".join(ket_qua))
# Bài 5.6
s = input("Nhập xâu: ")
tong_do_dai = len(s)

if tong_do_dai > 0:
    dac_biet = {}
    for c in s:
        # Không phải chữ cái (isalpha) và không phải số (isdigit)
        if not c.isalnum():
            dac_biet[c] = dac_biet.get(c, 0) + 1
            
    print(f"Tổng độ dài xâu: {tong_do_dai}")
    for ky_tu, so_lan in dac_biet.items():
        ty_le = (so_lan / tong_do_dai) * 100
        print(f"Ký tự '{ky_tu}' : {so_lan} lần -> Tỷ lệ: {ty_le:.2f}%")
# Bài 5.7
s = input("Nhập xâu: ")

thuong = hoa = so = dac_biet = 0
for c in s:
    if c.islower(): thuong += 1
    elif c.isupper(): hoa += 1
    elif c.isdigit(): so += 1
    else: dac_biet += 1 # Bao gồm cả khoảng trắng

print(f"Số chữ cái in thường: {thuong}")
print(f"Số chữ cái in hoa: {hoa}")
print(f"Số lượng chữ số: {so}")
print(f"Số lượng ký tự đặc biệt: {dac_biet}")
# Bài 5.8
s = input("Nhập xâu (vui lòng nhập dài hơn 10 ký tự): ")

if len(s) <= 10:
    print("Xâu nhập vào chưa đủ 10 ký tự!")
else:
    # Vị trí 2 đến 8 tương đương index 2 đến index 8
    print(f"+ Trích xuất từ vị trí 2 đến 8: {s[2:9]}") 
    print(f"+ 5 ký tự từ vị trí 5: {s[5:10]}")
    print(f"+ 3 ký tự cuối cùng: {s[-3:]}")
    print(f"+ Toàn bộ chữ HOA: {s.upper()}")
    print(f"+ Toàn bộ chữ thường: {s.lower()}")
    print(f"+ Đảo ngược xâu: {s[::-1]}")
# Bài 5.9
s1 = input("Nhập chuỗi ban đầu: ")
s2 = input("Nhập chuỗi mục tiêu: ")

m, n = len(s1), len(s2)
# Tạo ma trận quy hoạch động (m+1) x (n+1)
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Khởi tạo cột đầu và hàng đầu
for i in range(m + 1): dp[i][0] = i
for j in range(n + 1): dp[0][j] = j

# Tính toán ma trận
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] # Ký tự giống nhau, không tốn thao tác
        else:
            dp[i][j] = min(dp[i-1][j] + 1,    # Xóa
                           dp[i][j-1] + 1,    # Thêm
                           dp[i-1][j-1] + 1)  # Thay thế

print(f"-> Số thao tác (thêm, xóa, thay thế) tối thiểu cần thực hiện là: {dp[m][n]}")
# Bài 5.10
s = input("Nhập xâu dữ liệu: ")

# Xóa toàn bộ khoảng trắng, dấu cách, tab...
ket_qua = "".join(s.split())

print(f"Xâu sau khi loại bỏ khoảng trắng: {ket_qua}")



