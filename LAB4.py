#BÀI1:
n = int(input("Nhập n: "))
a, b = 0, 1
i = 1
while i < n:
    a, b = b, a + b
    i += 1
print("Số Fibonacci thứ", n, "là:", b)

#BÀI2:
password = ""
while password != "123456":
    password = input("Nhập mật khẩu: ")
print("Đăng nhập thành công!")

#BÀI3:
n = int(input("Nhập n: "))
i = n - 1
while i > 0:
    if n % i == 0:
        print("Ước lớn nhất (khác n) là:", i)
        break
    i -= 1

#BÀI4:
tong = 0
dem = 0
max_so = None
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break   
    tong += x
    dem += 1    
    if max_so is None or x > max_so:
        max_so = x
print("Tổng:", tong)
print("Số lượng:", dem)
print("Số lớn nhất:", max_so)

#BÀI5:
n = int(input("Nhập n: "))
temp = n
dao = 0

while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10

if dao == n:
    print("Đúng (Palindrome)")
else:
    print("Sai")

#BÀI6:
n = int(input("Nhập n: "))
temp = n
k = len(str(n))
tong = 0
while temp > 0:
    digit = temp % 10
    tong += digit ** k
    temp //= 10
if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong")

#BÀI7:
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print()
    i += 1

#BÀI8:
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

#BÀI9:
while True:
    print("\n===== MENU =====")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    choice = int(input("Chọn: "))
    if choice == 0:
        print("Thoát chương trình!")
        break
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if choice == 1:
        print("Kết quả:", a + b)
    elif choice == 2:
        print("Kết quả:", a - b)
    elif choice == 3:
        print("Kết quả:", a * b)
    elif choice == 4:
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ!")

#BÀI10:
n = int(input("Nhập số dòng: "))
i = n
while i > 0:
    print("*" * i)
    i -= 1

#BÀI11:
n = int(input("Nhập n (n > 10): "))
# a) S1 = 6 + 6^2 + ... + 6^a
S1 = 0
i = 1
while True:
    term = 6 ** i
    if term > n:
        break
    S1 += term
    i += 1
# b) S2 = 1/3 + 1/3^3 + ... + 1/3^(2a+1)
S2 = 0
i = 0
while True:
    term = 1 / (3 ** (2 * i + 1))
    if (3 ** (2 * i + 1)) > n:
        break
    S2 += term
    i += 1
# c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^a * a^2
S3 = 0
i = 1
while True:
    term = ((-1) ** i) * (i ** 2)
    if i ** 2 > n:
        break
    S3 += term
    i += 1
# d) S4 = 1*2*3 + 2*3*4 + ... + a(a+1)(a+2)
S4 = 0
i = 1
while True:
    term = i * (i + 1) * (i + 2)
    if term > n:
        break
    S4 += term
    i += 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)




