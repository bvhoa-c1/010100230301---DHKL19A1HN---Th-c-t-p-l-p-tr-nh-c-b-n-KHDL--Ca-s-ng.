# bài 1
n = int(input("Nhap n: "))

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
    print("Fibonacci thu", n, "la:", b)

# bài 2
password = ""

while password != "123456":
    password = input("Nhap mat khau: ")

print("Dang nhap thanh cong")    

# bài 3
n = int(input("Nhap n: "))

i = n - 1

while i > 0:
    if n % i == 0:
        print("Uoc lon nhat (khac n) la:", i)
        break
    i -= 1

# bài 4
tong = 0
dem = 0
max_num = None

while True:
    n = int(input("Nhap so: "))
    
    if n == 0:
        break
        
    tong += n
    dem += 1
    
    if max_num is None or n > max_num:
        max_num = n

print("Tong:", tong)
print("So luong:", dem)
print("So lon nhat:", max_num)    

# bài 5
n = int(input("Nhap n: "))
temp = n
dao = 0

while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10

if dao == n:
    print("La so doi xung")
else:
    print("Khong phai")

# bài 6
n = int(input("Nhap n: "))
temp = n
tong = 0

while temp > 0:
    digit = temp % 10
    tong += digit ** 3
    temp //= 10

if tong == n:
    print("La so Armstrong")
else:
    print("Khong phai")

# bài 7
i = 2

while i <= 9:
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i*j)
        j += 1
    print()
    i += 1

# bài 8
n = int(input("Nhap n: "))

tong = 0
tich = 1
dao = 0

while n > 0:
    digit = n % 10
    
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    
    n //= 10

print("Tong chu so:", tong)
print("Tich chu so:", tich)
print("So dao:", dao)

# bài 9
while True:
    print("1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("0. Thoat")
    
    chon = int(input("Chon: "))
    
    if chon == 0:
        break
        
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    
    if chon == 1:
        print("Ket qua:", a + b)
    elif chon == 2:
        print("Ket qua:", a - b)
    elif chon == 3:
        print("Ket qua:", a * b)
    elif chon == 4:
        if b != 0:
            print("Ket qua:", a / b)
        else:
            print("Khong chia duoc")

# bài 10
i = 4

while i > 0:
    print("*" * i)
    i -= 1