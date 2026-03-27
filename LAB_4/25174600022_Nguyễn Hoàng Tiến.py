#bài 1
n = int(input("nhập n in số dãy Fibonacci :"))
a = 0
b = 1
while a <= n:
    print(a, end = " ")
    a, b = b, a + b
print()
#bài 2
n = input("nhập mật khẩu 6 chữ số (123456): ")
mk = "123456"
while n != mk:
    n = input("sai mật khẩu, vui lòng nhập lại: ")
print("đúng mật khẩu!")

#bài 3
n = int(input("nhập số n: "))
a = 1
uoc_MAX = 0
while a < n:
    if n % a == 0:
        uoc_MAX = a
    a += 1
print("ước số lớn nhất của n là:", uoc_MAX)

#bài 4
tong = 0
so_luong = 0
so_max = None

while True:
    n = int(input("nhập số liên tục cho đến khi nhập số 0 thì dừng: "))
    if n == 0:
        break
    tong += n
    so_luong += 1
    if so_max is None or n > so_max:
        so_max = n

if so_luong == 0:
    print("Bạn chưa nhập số nào!")
else:
    print("tổng các số:", tong)
    print("tổng số lượng số:", so_luong)
    print("số lớn nhất:", so_max)

#bài 5
n = int(input("nhập số n: "))
so_dao = 0
so_goc = n
while n > 0:
    du = n % 10
    so_dao = so_dao * 10 + du
    n //= 10
print("số đảo:", so_dao)
if so_dao == so_goc:
    print(f"{so_goc} là số đối xứng!")
else:
    print(f"{so_goc} không phải số đối xứng!")

#bài 6
n = int(input("nhập n kiểm tra có phải số Armstrong hay ko: "))
mu = len(str(n))
so = 0
tong = 0
so_goc = n
while n >0:
    so = n % 10
    tong += so**mu
    n //= 10
if tong == so_goc:
    print(f"{so_goc} là số Armstrong")
else:
    print(f"{so_goc} ko phải là số Armstrong")

#bài 7
i = 1
j = 2
while True:
    while True:
        print(f"{j}x{i}={i*j}", end = "\t")
        j += 1
        if j > 9:
            break
    print()
    i += 1
    j = 2
    if i > 9:
        break

#bài 8
n = int(input("nhập số n: "))
so = 0
tong = 0
tich = 1
so_dao = 0
while n > 0:
    so = n % 10
    tong += so
    tich *= so
    so_dao = so_dao * 10 + so
    n //= 10
print("tổng chữ số: ", tong)
print("tích chữ số: ", tich)
print("số đảo: ", so_dao)

#bài 9
while True:
    print("------------CHƯƠNG TRÌNH MENU------------")
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    chon = int(input("chọn chức năng: "))

    if chon == 1:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        print("Kết quả:", a + b)

    elif chon == 2:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        print("Kết quả:", a - b)

    elif chon == 3:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        print("Kết quả:", a * b)

    elif chon == 4:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Không thể chia cho 0")
    elif chon == 0:
        break
    else:
        print("Lựa chọn không hợp lệ")

#bài 10
n = int(input("nhập vào chiều cao tam giác ngược: "))
while n > 0:
    print("x"*n)
    n -= 1
#bài 11
while True:
    n = int(input("nhập vào số n lớn hơn 10: "))
    if n > 10:
        break
a = 1
S1 = 0
S2 = 0
S3 = 0
S4 = 0
#a
while a < n:
    S1 += 6**a
    a += 1
print("kết quả S1 =",S1)
#b
a = 0
while a < n:
    S2 += 1/(3**(2*a+1))
    a += 1
print("kết quả S2 =",S2)
#c
a = 0
while a < n:
    S3 += (-1)**a * a**2
    a += 1
print("kết quả S3 =",S3)
#d
a = 0
while a < n:
    S4 += a*(a+1)*(a+2)
    a += 1
print("kết quả S4 =",S4)