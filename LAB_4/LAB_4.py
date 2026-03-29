
#Bài 1
n = int(input("Nhập n: "))
a = 0
b = 1
i = 2
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1
    print("Số fibonacci thứ", n, "la", b)

#Bài 2
while True:
    matkhau = input("Nhập mật khẩu: ")
    if matkhau == "123456":
        print("Đúng mật khẩu")
        break
    print("Sai mật khẩu, vui long nhập lại.")

#Bài 3
n = int(input("Nhập n: "))
i = n // 2
while i >= 1:
    if n % i == 0:
        print("Ước lớn nhất là:", i)
        break
    i -= 1

#Bài 4
tong = 0
dem = 0
max_num = None
while True:
    n = int(input("Nhập số: "))
    if n == 0:
        break
    tong += n
    dem += 1
    if max_num is None or n > max_num:
        max_num = n
print("Tổng:", tong)
print("Số lượng:", dem)
if dem > 0:
    print("Số lớn nhất:", max_num)
else:
    print("Không có số nào được nhập!")

#Bài 5
n = input("Nhập số n: ")
if n == n[::-1]:
    print(n, "là số đối xứng")
else:
    print(n, "không phải là số đối xứng")

#Bài 6
n = int(input("Nhập số: "))
original = n
tong = 0
while n > 0:
    digit = n % 10
    tong += digit ** 3
    n = n // 10
if tong == original:
    print("Là số armstrong")
else:
    print("Không là số armstrong")

#Bài 7
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j += 1
    print()
    i += 1

#Bài 8
n = int(input("Nhập số: "))
tong = 0
tich = 1
dao = 0
while n > 0:
    digit = n % 10
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    n = n // 10
print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)

#Bài 9
while True:
    print("\n----- MENU -----")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    chon = int(input("Chọn chức năng: "))
    if chon == 0:
        print("Thoát chương trình!")
        break
    if chon in [1, 2, 3, 4]:
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
                print("Lỗi: Không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

#Bài 10
n = 4
for i in range(n, 0, -1):
    print("*" * i)

#Bài 11
n = int(input("Nhập n (n > 10): "))

#a
S1 = 0
a = 1
while a <= n:
    S1 += 6 ** a
    a += 1
print("S1 =", S1)

#b
S2 = 0
a = 0
while a <= n:
    S2 += 1 / (3 ** (2*a + 1))
    a += 1
print("S2 =", S2)

#c
S3 = 0
a = 1
while a <= n:
    S3 += ((-1) ** a) * (a ** 2)
    a += 1
print("S3 =", S3)

#d
S4 = 0
a = 1
while a <= n:
    S4 += a * (a + 1) * (a + 2)
    a += 1
print("S4 =", S4)
