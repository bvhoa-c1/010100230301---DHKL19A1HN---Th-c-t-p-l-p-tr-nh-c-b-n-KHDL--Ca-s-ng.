# Bài 1:
n = int(input("Nhập n: "))
a, b = 0, 1
i = 0
while i < n:
    a, b = b, a + b
    i += 1
print("Số Fibonacci thứ", n, "là:", a)

# Bài 2:
while True:
    mat_khau = input("Nhập mật khẩu: ")
    
    if mat_khau == "123456":
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai mật khẩu, nhập lại!")

# Bài 3:
n = int(input("Nhập n: "))

i = n // 2

while i > 0:
    if n % i == 0:
        print("Ước số lớn nhất (khác n) là:", i)
        break
    i -= 1

#Bài 4:
tong = 0
dem = 0
max_so = None
while True:
    n = int(input("Nhập số (0 để dừng): "))
    
    if n == 0:
        break
    
    tong += n
    dem += 1
    
    if max_so is None or n > max_so:
        max_so = n

print("Tổng:", tong)
print("Số lượng:", dem)

if dem > 0:
    print("Số lớn nhất:", max_so)
else:
    print("Không có số nào được nhập!")

# Bài 5:
n = int(input("Nhập n: "))
temp = n
dao = 0
while temp > 0:
    digit = temp % 10
    dao = dao * 10 + digit
    temp //= 10
if dao == n:
    print("Đúng (số đối xứng)")
else:
    print("Sai (không phải số đối xứng)")

# Bài 6:
n = int(input("Nhập n: "))

temp = n
k = len(str(n))  # số chữ số
tong = 0

while temp > 0:
    digit = temp % 10
    tong += digit ** k
    temp //= 10

if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")

# Bài 7:
i = 2
while i <= 9:
    j = 1
    print("Bảng", i)
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j += 1
    i += 1

# Bài 8:
n = int(input("Nhập n: "))
temp = n
tong = 0
tich = 1
dao = 0
while temp > 0:
    digit = temp % 10
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    temp //= 10
print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)

# Bài 9:
while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    
    chon = int(input("Chọn chức năng: "))
    if chon == 0:
        print("Thoát chương trình!")
        break
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
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
            print("Không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ!")
        
# Bài 10:
i = 4
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1

# Bài 11:
n = int(input("Nhập n (n > 10): "))
# a) 
a = 1
S1 = 0
while a <= n:
    S1 += 6 ** a
    a += 1
# b) 
a = 0
S2 = 0
while a <= n:
    S2 += 1 / (3 ** (2*a + 1))
    a += 1
# c)
a = 1
S3 = 0
while a <= n:
    S3 += ((-1) ** a) * (a ** 2)
    a += 1
# d) 
a = 1
S4 = 0
while a <= n:
    S4 += a * (a + 1) * (a + 2)
    a += 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)