# Bài 1:
n = int(input("Nhập n: "))
a, b = 0, 1
i = 1
while i < n:
    a, b = b, a + b
    i += 1
print(f"Số Fibonacci thứ {n} là: {a}")

# Bài 2:
mat_khau = ""
while mat_khau != "123456":
    mat_khau = input("Nhập mật khẩu: ")
print("Đăng nhập thành công!")

# Bài 3:
n = int(input("Nhập n: "))
i = n - 1
while i >= 1:
    if n % i == 0:
        print(f"Ước lớn nhất khác n là: {i}")
        break
    i -= 1

# Bài 4:
tong = 0
dem = 0
max_so = None

while True:
    so = int(input("Nhập số (0 để dừng): "))
    if so == 0:
        break
    tong += so
    dem += 1
    if max_so is None or so > max_so:
        max_so = so

print(f"Tổng: {tong}, Số lượng: {dem}, Lớn nhất: {max_so}")

# Bài 5:
n_str = input("Nhập n: ")
if n_str == n_str[::-1]:
    print("Là số đối xứng")
else:
    print("Không đối xứng")

# Bài 6:
n = int(input("Nhập n: "))
s = str(n)
bac = len(s)
tong_arm = sum(int(chu_so)**bac for chu_so in s)

if tong_arm == n:
    print(f"{n} là số Armstrong")
else:
    print(f"{n} không phải số Armstrong")

# Bài 7:
i = 1
while i <= 10:
    j = 2
    while j <= 9:
        print(f"{j}x{i}={i*j:2d}", end="\t")
        j += 1
    print()
    i += 1

# Bài 8:
n = int(input("Nhập n: "))
temp = n
tong_cs = 0
tich_cs = 1
so_dao = 0

while temp > 0:
    chu_so = temp % 10
    tong_cs += chu_so
    tich_cs *= chu_so
    so_dao = so_dao * 10 + chu_so
    temp //= 10

print(f"Tổng: {tong_cs}, Tích: {tich_cs}, Số đảo: {so_dao}")

# Bài 9:
while True:
    print("\n1. Cộng | 2. Trừ | 3. Nhân | 4. Chia | 0. Thoát")
    chon = input("Chọn: ")
    if chon == "0": break
    
    a = float(input("Số thứ nhất: "))
    b = float(input("Số thứ hai: "))
    
    if chon == "1": print("Kết quả:", a + b)
    elif chon == "2": print("Kết quả:", a - b)
    elif chon == "3": print("Kết quả:", a * b)
    elif chon == "4": print("Kết quả:", a / b if b != 0 else "Lỗi chia cho 0")

# Bài 10:
n = int(input("Nhập số hàng: "))
for i in range(n, 0, -1):
    print("*" * i)
n = int(input("Nhập vào số nguyên n (n > 10): "))

# a)
s1 = 0
a = 1
while a <= n:
    s1 += 6**a
    a += 1
print(f"S1 = {s1}")

# b)
s2 = 0
a = 0
while a <= n:
    s2 += 1 / (3**(2*a + 1))
    a += 1
print(f"S2 = {s2}")

# c)
s3 = 0
a = 1
while a <= n:
    s3 += ((-1)**a) * (a**2)
    a += 1
print(f"S3 = {s3}")

# d)
s4 = 0
a = 1
while a <= n:
    s4 += a * (a + 1) * (a + 2)
    a += 1
print(f"S4 = {s4}")