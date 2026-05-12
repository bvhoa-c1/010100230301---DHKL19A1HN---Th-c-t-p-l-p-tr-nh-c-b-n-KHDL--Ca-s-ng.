#BÀI 1:
n = int(input("Nhập n: "))
a, b = 0, 1
i = 0
while i < n:
    a, b = b, a + b
    i += 1
print("Fibionacci thứ", n, "Là:", a)

#BÀI 2:
mat_khau = ""
while mat_khau != "123456":
    mat_khau = input("Nhạp mật khẩu: ")
print("Đăng nhập thành công!")

#BÀi 3:
n = int(input("Nhập n: "))
i = n - 1
while i > 0:
    if n % i == 0:
        print("Ước lớn nhất (Khác n ): ", i)
        break
    i -= 1

#BÀi 4:
tong = 0
so_luong = 0
so_lon_nhat = None
while True:
    x = int(input("Nhập số (0 để dừng): "))    
    if x == 0:
        break   
    tong += x
    so_luong += 1    
    if so_lon_nhat is None or x > so_lon_nhat:
        so_lon_nhat = x
print("Tổng:", tong)
print("Số lượng:", so_luong)
print("Số lớn nhất:", so_lon_nhat)

#BÀi 5:
n = int(input("Nhập n: "))
bien_tam_thoi = n
so_dao = 0
while bien_tam_thoi > 0:
    so_dao = so_dao * 10 + bien_tam_thoi % 10
    bien_tam_thoi //= 10
if so_dao == n:
    print("Là số đối xứng")
else:
    print("Không phải số đối xứng")

#BÀI 6:
n = int(input("Nhập n: "))
bien_tam_thoi = n
tong = 0
so_chu_so = len(str(n))
while bien_tam_thoi > 0:
    chu_so = bien_tam_thoi % 10
    tong += chu_so ** so_chu_so
    bien_tam_thoi //= 10
if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")

#BÀi 7:
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i*j)
        j += 1
    print()
    i += 1

#BÀI 8:
n = int(input("Nhập n: "))
tong = 0
tich = 1
so_dao = 0
bien_tam_thoi = n
while bien_tam_thoi > 0:
    chu_so = bien_tam_thoi % 10
    tong += chu_so
    tich *= chu_so
    so_dao = so_dao * 10 + chu_so
    bien_tam_thoi //= 10
print("Tổng chữ số: ", tong)
print("Tích chữ số: ", tich)
print("Số đảo: ", so_dao)

#BÀI 9:
while True:
    print("\n1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    lua_chon = int(input("Chọn: "))
    if lua_chon == 0:
        break
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if lua_chon == 1:
        print("Kết quả:", a + b)
    elif lua_chon == 2:
        print("Kết quả:", a - b)
    elif lua_chon == 3:
        print("Kết quả:", a * b)
    elif lua_chon == 4:
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Không chia được cho 0")

#BÀi 10:
n = int(input("Nhập số hàng: "))
i = n
while i > 0:
    print("*" * i)
    i -= 1

#BÀi 11:
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

