# bài 1 :
n = int(input("Nhập n : "))
a, b = 0, 1
i = 1
while i < n:
    a, b = b, a + b
    i += 1

print(a)

# bài 2 
password = ""

while password != "123456":
    password = input("Nhập mật khẩu: ")

print("Đúng rồi!")

# bài 3 :
n = int(input("Nhập số n : "))
i = n - 1
while i > 0:
    if n % i == 0:
        break
    i -= 1
print(i)
# bài 4 :
tong = 0
dem = 0
max_val = None
while True:
    x = int(input("Nhập x : "))   
    if x == 0:
        break   
    tong += x
    dem += 1  
    if max_val is None or x > max_val:
        max_val = x
print("Tổng:", tong)
print("Số lượng:", dem)
print("Max:", max_val)

# bài 5 :
n = input("NHập số n : ")

rev = ""
i = len(n) - 1

while i >= 0:
    rev += n[i]
    i -= 1

if n == rev:
    print("đúng")
else:
    print("sai")

# bài 6 :
n = int(input("Nhập n : "))
tong = 0
while n > 0:
    du = n % 10
    tong += n ** 3
    n //= 10

if tong == n:
    print("đúng")
else:
    print("sai")

# bài 7 :
i = 2
while i <= 9:
    print("Bảng", i)    
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j += 1   
    print() 
    i += 1

# bài 8 :
n = int(input("Nhập số n : "))
tong = 0
tich = 1
dao = 0
while n > 0:
    du = n % 10   
    tong += du
    tich *= du
    dao = dao * 10 + du   
    n //= 10
print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)

# bài 9 :
while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    
    choice = int(input("Chọn: "))
    
    if choice == 0:
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
            print("lỗi")
    else:
        print("Chọn sai!")

# bài 10 :
n = int(input("Nhập n : "))
i = n
while i > 0:
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print()
    i -= 1

# bài 11 :
n = int(input("Nhập số nguyên n : "))
# a) 
S1 = 0
i = 1

while True:
    term = 6 ** i
    if term > n:
        break
    S1 += term
    i += 1

print("S1 =", S1)


# b) 
S2 = 0
i = 0

while True:
    power = 2 * i + 1
    term = 1 / (3 ** power)
    if 3 ** power > n:
        break
    S2 += term
    i += 1

print("S2 =", S2)


# c) 
S3 = 0
i = 1

while True:
    term = i ** 2
    if term > n:
        break
    
    if i % 2 == 0:
        S3 += term
    else:
        S3 -= term
    
    i += 1

print("S3 =", S3)


# d) 
S4 = 0
i = 1

while True:
    term = i * (i + 1) * (i + 2)
    if term > n:
        break
    S4 += term
    i += 1

print("S4 =", S4)