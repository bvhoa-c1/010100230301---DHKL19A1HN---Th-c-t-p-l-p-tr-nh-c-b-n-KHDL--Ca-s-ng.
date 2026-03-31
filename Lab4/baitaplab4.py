
#Bai1:
n = int(input("Nhập n: "))
a, b = 0, 1
count = 1
while count < n:
    a, b = b, a + b
    count += 1
print(f"Số Fibonacci thứ {n} là: {a}") 

#Bai2:
while True:
    mat_khau = input("Nhập mật khẩu: ")
    
    if mat_khau == "123456":
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai mật khẩu, nhập lại!")

#Bai3:
n = int(input("Nhập n:"))
i = n-1
while i >0:
    if n %i ==0:
        print(f"Ước lớn nhất khác {n} là: {i}")
        break
    i-=1

#Bai4:
tong=0
dem=0
lon_nhat=None
while True:
    n = float(input("Nhâp số (nhập 0 để dừng): "))
    if n==0:
        break
    tong+=n
    dem+=1
    if lon_nhat is None or n>lon_nhat:
        lon_nhat=n
print(f"Tổng: {tong}, Số lượng:{dem}, Lớn nhất:{lon_nhat}")

#Bai5:
n = int(input("Nhập n: "))
temp = n
so_dao = 0
while temp > 0:
    so_dao = so_dao * 10 + (temp % 10)
    temp //= 10
print("Đúng" if n == so_dao else "Sai")

#Bai6:
n = int(input("Nhập n: "))
s = str(n)
bac = len(s)
tong = 0
temp = n
while temp > 0:
    tong += (temp % 10) ** bac
    temp //= 10
print(f"{n} là số Armstrong" if tong == n else f"{n} không phải số Armstrong")

#Bai7:
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print("-" * 10)
    i += 1

#Bai8:
n = int(input("Nhập n: "))
tong = 0
tich = 1
so_dao = 0
while n > 0:
    chu_so = n % 10
    tong += chu_so
    tich *= chu_so
    so_dao = so_dao * 10 + chu_so
    n //= 10
print(f"Tổng: {tong}, Tích: {tich}, Số đảo: {so_dao}")

#Bai9:
while True:
    print("\n1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    chon = input("Chọn: ")
    if chon == '0': break
    a = float(input("Số a: "))
    b = float(input("Số b: "))
    if chon == '1': 
        print("Kết quả:", a + b)
    elif chon == '2': 
        print("Kết quả:", a - b)
    elif chon == '3': 
        print("Kết quả:", a * b)
    elif chon == '4': 
        print("Kết quả:", a / b if b != 0 else "Lỗi chia cho 0")

#Bai10:
n = int(input("Nhập n: "))
while n > 0:
    print("*" * n)
    n -= 1

#Bai11:
n = int(input("Nhập n>10: "))
#a
s1 = 0
i = 1
while i <= n:
    s1 += 6**i
    i += 1
print(f"S1 = {s1}")
#b
s2 = 0
i = 0 
while i <= n:
    s2 += 1 / (3**(2*i + 1))
    i += 1
print(f"S2 = {s2}")
#c
s3 = 0
i = 1
while i <= n:
    if i % 2 == 0:
        s3 += i**2
    else:
        s3 -= i**2
    i += 1
print(f"S3 = {s3}")
#d
s4 = 0
i = 1
while i <= n:
    s4 += i * (i + 1) * (i + 2)
    i += 1
print(f"S4 = {s4}")