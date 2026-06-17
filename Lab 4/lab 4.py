# Bài 1:
n = int(input("Nhập n: "))
a, b = 0, 1
i = 0
while i < n:
    a, b = b, a+b
    i += 1
print("Fibonacci thứ ", n, "là:", a)
# Bài 2:
mat_khau = ""
while mat_khau != "123456":
    mat_khau = input("Nhập mật khẩu:")
print("Dúng mật khẩu")
# Bài 3:
n = int(input("Nhập n: "))
i = n-1
while i > 0:
    if n % i == 0:
        print("Ước lớn nhất (khác n):", i)
    i -= 1
# Bài 4
tong = 0
dem = 0
max_so = None
while True:
    x = int(input("Nhập số (0 để dừng):"))
    if x == 0:
        break
    tong += x
    dem += 1
    if max_so is None or x > max_so:
        max_so = x
print("Tổng:", tong)
print("Số lượng:", dem)
print("Max:", max_so)
# bài 5:
n = int(input("Nhập n:"))
temp = n
dao = 0
while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10
if dao == n:
    print("Là số đối xứng:")
else:
    print("Không phải")
# Bài 6:
n = int(input("Nhập n:"))
temp = 0
tong = 0
so_chu_so = len(str(n))
while temp > 0:
    tong += (temp % 10) ** so_chu_so
    temp //= 0
if tong == n:
    print("Là số amstrong")
else:
    print("Không phải")
#Bài 7:
i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i*j:4}", end="")
        j += 1
    print()
    i += 1
# Bài 8:
n = int(input("Nhập n:"))
temp = n
tong = 0
tich = 1
dao = 0
while temp > 0:
    chu_so = temp % 10
    tong += chu_so
    tich *= chu_so
    dao = dao * 10 + chu_so
    temp //= 10
print("Tổng:",tong)
print("Tích:", tich)
print("Số đảo:", dao)
# Bài  9:
while True:
    print("\n1.Cộng")
    print("2.Trừ")
    print("3.Nhân")
    print("4.Chia")
    print("0.Thoát")
    chon = int(input("Chpn"))
    if chon == 0:
        break
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    if chon == 1:
        print("Kết quả:", a + b)
    elif chon == 2:
        print("Kết quả:", a - b)
    elif chon == 3:
        print("Kết quả:", a * b)
    elif chon == 4:
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Không chia được")
# Bài 10
n = int(input("Nhập số hàng: "))
while n > 0:
    print("*" * n)
    n -= 1
# Bài 11:
#a
n = int(input("Nhập n (>10): "))
s1 = 0
a = 1
while a <= n:
    s1 += 6**a
    a += 1
print(f"S1 = {s1}")
#b
s2 = 0
a = 0
while a <= n:
    s2 += 1 / (3**(2*a + 1))
    a += 1
print(f"S2 = {s2}")
#c
s3 = 0
a = 1
while a <= n:
    s3 += ((-1)**a) * (a**2)
    a += 1
print(f"S3 = {s3}")
#d
s4 = 0
a = 1
while a <= n:
    s4 += a * (a + 1) * (a + 2)
    a += 1
print(f"S4 = {s4}")
