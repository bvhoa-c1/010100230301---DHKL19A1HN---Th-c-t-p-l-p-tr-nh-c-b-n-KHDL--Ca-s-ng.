# bài 1
"""n = int(input("nhập n :"))
a, b = 0, 1
i = 1
while i < n:
    a, b = b, a+ b
    i += 1
print("fibonacci thứ", n, "là:", a)

# bài 2
while True:
    mk = input(" nhập mật khẩu:")
    if mk == "123456":
        print("đúng rồi!")
        break
    else:
        print("sai, nhập lại!")

# bài 3
n = int(input("nhập n :"))
i = n - 1
while i > 0:
    if n % i == 0:
        print("ước lớn nhất (khác n):", i)
        break
    i -= 1

# bài 4
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
print("Số lớn nhất:", max_val)

# bài 5
n = int(input("Nhập n: "))
temp = n
dao = 0

while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10

if dao == n:
    print("Là số đối xứng")
else:
    print("Không phải")

# bài 6
n = int(input("Nhập n: "))
temp = n
tong = 0

while temp > 0:
    digit = temp % 10
    tong += digit ** 3
    temp //= 10

if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải")

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
n = int(input("Nhập số nguyên n: "))
temp = n
tong = 0
tich = 1 if n != 0 else 0
so_dao = 0

while temp > 0:
    chu_so = temp % 10
    tong += chu_so
    tich *= chu_so
    so_dao = so_dao * 10 + chu_so
    temp //= 10

print(f"Tổng chữ số: {tong}")
print(f"Tích chữ số: {tich}")
print(f"Số đảo: {so_dao}")

# bài 9
while True:
    print("\n--- MENU ---")
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    chon = input("Chọn chức năng: ")

    if chon == '0': break
    
    if chon in ['1', '2', '3', '4']:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        if chon == '1': print(f"Kết quả: {a + b}")
        elif chon == '2': print(f"Kết quả: {a - b}")
        elif chon == '3': print(f"Kết quả: {a * b}")
        elif chon == '4': 
            print(f"Kết quả: {a / b}" if b != 0 else "Lỗi chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ.")

# bài 10
for i in range(4, 0, -1):
    print("*" * i)"""

# bài 11
#a
n = int(input("Nhập n (>10): "))
s1 = 0
a = 1
while a <= n:
    s1 += 6**a
    a += 1
print(f"S1 = {s1}")
#b
s2 = 0
a = 0
while a <= n:
    s2 += 1 / (3**(2*a + 1))
    a += 1
print(f"S2 = {s2}")
#c
s3 = 0
a = 1
while a <= n:
    s3 += ((-1)**a) * (a**2)
    a += 1
print(f"S3 = {s3}")
#d
s4 = 0
a = 1
while a <= n:
    s4 += a * (a + 1) * (a + 2)
    a += 1
print(f"S4 = {s4}")


