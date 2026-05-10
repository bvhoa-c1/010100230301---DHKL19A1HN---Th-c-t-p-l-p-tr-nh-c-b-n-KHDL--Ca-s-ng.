# bài 1
n = int(input("Nhập n: "))
a, b = 0, 1
i = 1
if n == 1:
    print(a)
else:
    while i < n-1:
        a, b = b, a + b
        i += 1
    print(b)
# bài 2 
password = ""
while password != "123456":
    password = input("Nhập mật khẩu: ")
print("Đăng nhập thành công!")
# bài 3
n = int(input("Nhập n: "))
i = n - 1
while i > 0:
    if n % i == 0:
        print("Ước số lớn nhất của", n, "là", i)
        break
    i -= 1
# bài 4
tong = 0
dem = 0
max_so = None
x = int(input("Nhập số (0 để dừng): "))
while x != 0:
    tong += x
    dem += 1
    if max_so is None or x > max_so:
        max_so = x
    x = int(input("Nhập số (0 để dừng): "))
print("Tổng:", tong)
print("Số lượng:", dem)
print("Số lớn nhất:", max_so)
# bài 5
n = int(input("Nhập n: "))
temp = n
dao = 0
while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10
if dao == n:
    print("Đúng, là số palindrome")
else:
    print("Sai, không phải số palindrome")
# bài 6
n = int(input("Nhập n: "))
temp = n
tong = 0
while temp > 0:
    chu_so = temp % 10
    tong += chu_so ** 3
    temp //= 10
if tong == n:
    print(n, "là số Armstrong")
else:
    print(n, "không phải số Armstrong")
# bài 7
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print()
    i += 1
# bài 8
n = int(input("Nhập n: "))
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
print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)
# bài 9
while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    choice = int(input("Chọn: "))
    if choice == 0:
        break
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
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
            print("Lỗi: chia cho 0")
    else:
        print("Lựa chọn không hợp lệ")
# bài 10
n = 4
while n > 0:
    print("*" * n)
    n -= 1