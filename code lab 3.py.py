# BÀI 1:
tong_a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong_a += i
print(tong_a)

tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print(tong_b)
# BÀI 2:
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}x{i}={i*j}", end="\t")
    print()
# BÀI 3:
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or i == n or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# BÀI 4:
import math

while True:
    n = int(input())
    if n > 0:
        break

s1 = 0
for i in range(1, n + 1):
    s1 += i
print(s1)

s2 = 0
for i in range(1, n + 1):
    s2 += 1/i
print(s2)

s3 = 0
for i in range(1, n + 1):
    s3 += 1 / math.sqrt(2 * i)
print(s3)

s4 = 0
for i in range(1, n + 1):
    s4 += ((-1)**(i + 1)) / i
print(s4)
# BÀI 5:
for i in range(1, 1001):
    if int(i**0.5)**2 == i:
        print(i, end=" ")
print()
# BÀI 6:
n = int(input())
s1 = 0
for i in range(1, n + 1):
    s1 += 1/i
print(s1)
# BÀI 7:
n = int(input())
dem = 0
for i in range(1, n + 1):
    tong_chu_so = 0
    temp = i
    while temp > 0:
        tong_chu_so += temp % 10
        temp //= 10
    if tong_chu_so % 2 == 0:
        dem += 1
print(dem)
# BÀI 8:
n = int(input())
max_sum = -1
result_num = 0

for i in range(1, n + 1):
    tong = sum(int(chuso) for chuso in str(i))
    if tong > max_sum:
        max_sum = tong
        result_num = i
print(result_num)
# BÀI 9:
n = int(input())
max_uoc = 0
result_num = 0

for i in range(1, n + 1):
    dem_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        result_num = i
print(result_num)
# BÀI 11:
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
# BÀI 12:
# Nhập chuỗi 10 ký tự 
s = input().upper()

# Bảng mã hóa chữ cái 
ma_chu = "ABCDEFGHIJK LMNOPQRSTU VWXYZ"
so_tuong_ung = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 0, 34, 35, 36, 37, 38]

tong = 0

# Bước 1 & 2: Chạy vòng lặp tính trọng số và cộng dồn vào tổng
for i in range(10):
    ky_tu = s[i]
    
    if 'A' <= ky_tu <= 'Z':
        # Tìm vị trí chữ cái trong bảng để lấy số tương ứng
        idx = ma_chu.find(ky_tu)
        val = so_tuong_ung[idx]
    else:
        # Nếu là số thì giữ nguyên giá trị
        val = int(ky_tu)
    
    # Tính trọng số: giá trị * 2^i
    trong_so = val * (2**i)
    tong += trong_so

# Bước 3: Lấy tổng chia cho 11 lấy số dư
check_digit = tong % 11

# Nếu dư 10 thì kết quả bằng 0# Nhập chuỗi 10 ký tự (Ví dụ: SUDU307007)
s = input().upper()

# Bảng mã hóa chữ cái (đã bỏ qua 11, 22, 33)
ma_chu = "ABCDEFGHIJK LMNOPQRSTU VWXYZ"
so_tuong_ung = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 0, 34, 35, 36, 37, 38]

tong = 0

# Bước 1 & 2: Chạy vòng lặp tính trọng số và cộng dồn vào tổng
for i in range(10):
    ky_tu = s[i]
    
    if 'A' <= ky_tu <= 'Z':
        # Tìm vị trí chữ cái trong bảng để lấy số tương ứng
        idx = ma_chu.find(ky_tu)
        val = so_tuong_ung[idx]
    else:
        # Nếu là số thì giữ nguyên giá trị
        val = int(ky_tu)
    
    # Tính trọng số: giá trị * 2^i
    trong_so = val * (2**i)
    tong += trong_so

# Bước 3: Lấy tổng chia cho 11 lấy số dư
check_digit = tong % 11

# Nếu dư 10 thì kết quả bằng 0
if check_digit == 10:
    check_digit = 0

print(f"Số kiểm tra: {check_digit}")
if check_digit == 10:
    check_digit = 0

print(f"Số kiểm tra: {check_digit}")