# BÀI 1:
n = int(input())

if n <= 1:
    print(n)
else:
    a, b = 0, 1
    count = 1
    while count < n:
        temp = a + b
        a = b
        b = temp
        count += 1
    print(b)
# BÀI 2:
mat_khau = ""
while mat_khau != "123456":
    mat_khau = input("Nhập mật khẩu: ")

print("Đăng nhập thành công!")
# BÀI 3:
n = int(input())
uoc = n - 1

while uoc > 0:
    if n % uoc == 0:
        print(uoc)
        break
    uoc -= 1
# BÀI 4:
tong = 0
dem = 0
max_so = None

while True:
    n = int(input("Nhập số: "))
    if n == 0:
        break
    
    tong += n
    dem += 1
    
    if max_so is None or n > max_so:
        max_so = n

print(f"Tổng: {tong}")
print(f"Số lượng: {dem}")
print(f"Số lớn nhất: {max_so}")
# BÀI 5:
n = int(input("Nhập n: "))
temp = n
so_dao = 0

while temp > 0:
    chu_so = temp % 10
    so_dao = so_dao * 10 + chu_so
    temp //= 10

if n == so_dao:
    print("đúng")
else:
    print("sai")
# BÀI 6:
n = int(input("Nhập n: "))
temp = n
tong_mu = 0
# Lấy số lượng chữ số để làm số mũ
so_chu_so = len(str(n))

temp2 = n
while temp2 > 0:
    chu_so = temp2 % 10
    tong_mu += chu_so ** so_chu_so
    temp2 //= 10

if n == tong_mu:
    print("là số Armstrong")
else:
    print("không phải số Armstrong")
# BÀI 7:
i = 1
while i <= 10:
    j = 2
    while j <= 9:
        print(f"{j} x {i} = {i*j}", end="\t")
        j += 1
    print()
    i += 1
# BÀI 8:
n = int(input("Nhập n: "))
tong = 0
tich = 1
so_dao = 0
temp = n

while temp > 0:
    chu_so = temp % 10
    tong += chu_so
    tich *= chu_so
    so_dao = so_dao * 10 + chu_so
    temp //= 10

print(f"Tổng: {tong}, Tích: {tich}, Số đảo: {so_dao}")
# BÀI 9:
while True:
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    chon = input("Chọn: ")
    if chon == '0': break
    if chon in ['1', '2', '3', '4']:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        if chon == '1': print(f"Kết quả: {a + b}")
        elif chon == '2': print(f"Kết quả: {a - b}")
        elif chon == '3': print(f"Kết quả: {a * b}")
        elif chon == '4': print(f"Kết quả: {a / b if b != 0 else 'Lỗi chia cho 0'}")
# BÀI 10:
n = int(input("Nhập số hàng: "))
while n > 0:
    print("*" * n)
    n -= 1
# BÀI 11:
n = int(input("Nhập n (>10): "))
a = 1
s1 = s2 = s3 = s4 = 0

while a <= n:
    s1 += 6**a
    s2 += 1 / (3**(2*a - 1))
    s3 += ((-1)**a) * (a**2)
    s4 += a * (a + 1) * (a + 2)
    a += 1

print(f"S1: {s1}\nS2: {s2}\nS3: {s3}\nS4: {s4}")