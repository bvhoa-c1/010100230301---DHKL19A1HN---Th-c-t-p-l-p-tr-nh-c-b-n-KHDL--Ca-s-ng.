#Bài 1: Fibonacci thứ n (while)
n = int(input("Nhập n: "))

a, b = 0, 1
i = 1

while i < n:
    a, b = b, a + b
    i += 1

print("Fibonacci thứ", n, "=", a)
# Bài 2: Nhập mật khẩu
while True:
    mk = input("Nhập mật khẩu: ")
    if mk == "123456":
        print("Đúng mật khẩu!")
        break
    else:
        print("Sai, nhập lại!")
# Bài 3: Ước số lớn nhất (khác n)
n = int(input("Nhập n: "))

i = n - 1
while i >= 1:
    if n % i == 0:
        print("Ước lớn nhất (khác n):", i)
        break
    i -= 1
# Bài 4: Nhập đến khi gặp 0
tong = 0
dem = 0
max_val = None

while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    
    tong += x
    dem += 1
    
    if max_val is None or x > max_val:
        max_val = x

print("Tổng:", tong)
print("Số lượng:", dem)
print("Max:", max_val)
# Bài 5: Số đối xứng
n = int(input("Nhập n: "))
s = str(n)

if s == s[::-1]:
    print("Là số đối xứng")
else:
    print("Không phải")
# Bài 6: Số Armstrong
n = int(input("Nhập n: "))
s = str(n)
k = len(s)

tong = 0
i = 0

while i < k:
    tong += int(s[i]) ** k
    i += 1

if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải")
# Bài 7: Bảng cửu chương (while lồng)
i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print("------")
    i += 1
# Bài 8: Tách chữ số
n = int(input("Nhập n: "))

tong = 0
tich = 1
dao = 0

temp = n

while temp > 0:
    d = temp % 10
    tong += d
    tich *= d
    dao = dao * 10 + d
    temp //= 10

print("Tổng:", tong)
print("Tích:", tich)
print("Đảo:", dao)
# Bài 9: Menu
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
        print("KQ:", a + b)
    elif chon == 2:
        print("KQ:", a - b)
    elif chon == 3:
        print("KQ:", a * b)
    elif chon == 4:
        if b != 0:
            print("KQ:", a / b)
        else:
            print("Không chia được cho 0")
# Bài 10: Tam giác ngược
n = int(input("Nhập số dòng: "))

i = n
while i >= 1:
    print("*" * i)
    i -= 1
#bài11
n = int(input("Nhập n (n > 10): "))

# a) S1 = 6 + 6^2 + 6^3 + ... + 6^k (dừng khi > n)
S1 = 0
i = 1
while True:
    term = 6 ** i
    S1 += term
    if S1 > n:
        break
    i += 1
print("S1 =", S1)


# b) S2 = 1/3 + 1/3^3 + 1/3^5 + ... (dừng khi > n)
S2 = 0
i = 1
while True:
    term = 1 / (3 ** (2*i - 1))
    S2 += term
    if S2 > n:
        break
    i += 1
print("S2 =", S2)


# c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^i * i^2 (dừng khi > n)
S3 = 0
i = 1
while True:
    term = ((-1) ** i) * (i ** 2)
    S3 += term
    if abs(S3) > n:
        break
    i += 1
print("S3 =", S3)


# d) S4 = 1*2*3 + 2*3*4 + ... + i*(i+1)*(i+2)
S4 = 0
i = 1
while True:
    term = i * (i + 1) * (i + 2)
    S4 += term
    if S4 > n:
        break
    i += 1
print("S4 =", S4)
