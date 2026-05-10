#Bài 1
n = int(input("Nhập n: "))
a, b = 0, 1
i = 1

while i < n:
    a, b = b, a + b
    i += 1

print("Fibonacci =", a)
#Bài 2
while True:
    mk = input("Nhập mật khẩu: ")
    if mk == "123456":
        print("Đúng!")
        break
#Bài 3
n = int(input("Nhập n: "))
i = n - 1

while i > 0:
    if n % i == 0:
        print("Ước lớn nhất:", i)
        break
    i -= 1
#Bài 4
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
#Bài 5
n = input("Nhập số: ")

if n == n[::-1]:
    print("Đúng")
else:
    print("Sai")
#Bài 6
n = input("Nhập số: ")
k = len(n)
tong = 0

for i in n:
    tong += int(i) ** k

if tong == int(n):
    print("Là Armstrong")
else:
    print("Không phải")
#Bài 7
i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i}x{j}={i*j}", end="  ")
        j += 1
    print()
    i += 1
#Bài 8
n = int(input("Nhập n: "))

tong = 0
tich = 1
dao = 0

while n > 0:
    digit = n % 10
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    n //= 10

print("Tổng:", tong)
print("Tích:", tich)
print("Đảo:", dao)
#Bài 9
while True:
    print("1.Cộng 2.Trừ 3.Nhân 4.Chia 0.Thoát")
    chon = int(input("Chọn: "))

    if chon == 0:
        break

    a = float(input("a = "))
    b = float(input("b = "))

    if chon == 1:
        print(a + b)
    elif chon == 2:
        print(a - b)
    elif chon == 3:
        print(a * b)
    elif chon == 4:
        if b != 0:
            print(a / b)
        else:
            print("Không chia được")
#Bài 10
n = int(input("Nhập n: "))

while n > 0:
    print("*" * n)
    n -= 1