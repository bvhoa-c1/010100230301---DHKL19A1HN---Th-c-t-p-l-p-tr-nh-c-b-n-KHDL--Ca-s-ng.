#Bai 1
n = int(input("Nhập n: "))
a = 0
b = 1
i = 1
while i < n:
    a, b = b, a + b
    i += 1
print("Fibonacci thứ", n, "là:", b)
#Bai 2
mk = ""
while mk != "123456":
    mk = input("Nhập mật khẩu: ")
print("Đúng mật khẩu")
#Bai 3
n = int(input("Nhập n: "))
i = n - 1
while i > 0:
    if n % i == 0:
        print("Ước lớn nhất (khác n):", i)
        break
    i -= 1
#Bai 4
tong = 0
dem = 0
max_val = None
while True:
    x = int(input("Nhập số: "))
    if x == 0:
        break
    tong += x
    dem += 1
    if max_val is None or x > max_val:
        max_val = x
print("Tổng:", tong)
print("Số lượng:", dem)
print("Số lớn nhất:", max_val)
#Bai 5
n = int(input("Nhập n: "))
temp = n
dao = 0
while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10
if dao == n:
    print("Đúng (đối xứng)")
else:
    print("Sai (không đối xứng)")
#Bai 6
n = int(input("Nhập n: "))
temp = n
k = 0
t = n
while t > 0:
    k += 1
    t //= 10
tong = 0
while temp > 0:
    digit = temp % 10
    tong += digit ** k
    temp //= 10
if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")
#Bai 7
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j += 1
    print()
    i += 1
#Bai 8
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
#Bai 9
while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    chon = int(input("Chọn: "))
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
            print("Không chia được cho 0")

#Bai 10
n = int(input("Nhập số dòng: "))
i = n
while i > 0:
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print()
    i -= 1

#Bai 11
n = int(input("Nhập n (n > 10): "))
#a.
S1 = 0
a = 1
while a <= n:
    S1 += 6 ** a
    a += 1
#b.
S2 = 0
a = 1
while a <= n:
    S2 += 1 / (3 ** (2*a - 1))
    a += 1
#c.
S3 = 0
a = 1
while a <= n:
    S3 += ((-1) ** a) * (a ** 2)
    a += 1
#d.
S4 = 0
a = 1
while a <= n:
    S4 += a * (a + 1) * (a + 2)
    a += 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
