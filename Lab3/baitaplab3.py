
#Bai1:
#a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng (a) là:", tong)
#b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng (b) là:", tong)

#Bai2:
for i in range(1, 10):
    for j in range(1, 11):
        print(f" {i} x {j} = {i*j}")
    print()

#Bai3:
n = int(input("Nhập vào số hàng: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or i == n or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()

#Bai4:
n = int(input("Nhap so nguyen duong:"))
if n <= 0: 
    print("Nhap sai, yeu cau nhap lai")
#a
S1=0
for i in range(1,n+1):
    S1+=i
print("Tong S1 = ",S1)

#b
S2=0
for i in range(1,n+1):
    S2+=1/i
print("Tong S2 = ",S2)

#c
S3=0
for i in range(1,n+1):
    S3+=(1/(2*i)**0.5)
print("Tong S3 = ",S3)

#d
S4=0
for i in range(1,n+1):
    S4+=((-1)*(i+1)/i)
print("Tong S4 = ",S4)

#Bai5:
print("Cac so chinh phuong tu 1 đến 1000:")
for i in range(1,1001):
    if (i**0.5) == int(i**0.5):
        print(i,end=" ")

#Bai6:
n = int(input("Nhap n:"))
S=0
for i in range(1,n+1):
    S+=1/i
print("Tong nghich dao S = ",S)

#Bai7:
n = int(input("Nhập n: "))
dem = 0
for i in range(1, n + 1):
    tong_chu_so = sum(int(ch) for ch in str(i))
    if tong_chu_so % 2 == 0:
        dem += 1
print(f"Có {dem} số có tổng chữ số là số chẵn.")

#Bai8:
n = int(input("Nhập n: "))
max_tong = -1
so_tim_duoc = 0

for i in range(1, n + 1):
    tong_chu_so = sum(int(ch) for ch in str(i))
    if tong_chu_so > max_tong:
        max_tong = tong_chu_so
        so_tim_duoc = i

print(f"Số có tổng chữ số lớn nhất là {so_tim_duoc} (Tổng = {max_tong})")

#Bai9:
n = int(input("Nhập n: "))
max_uoc = 0
so_nhieu_uoc_nhat = 0

for i in range(1, n + 1):
    dem_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_nhieu_uoc_nhat = i

print(f"Số có nhiều ước nhất là {so_nhieu_uoc_nhat} với {max_uoc} ước.")

#Bai11:
n = int(input("Nhập n số Fibonacci cần in: "))
a, b = 0, 1
print(f"{n} số Fibonacci đầu tiên là:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Bai12:
bang_ma = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

container = input("Nhập mã container (10 ký tự): ").upper()

tong_trong_so = 0

for i in range(10):
    ky_tu = container[i]
    
    if ky_tu.isalpha():
        gia_tri = bang_ma[ky_tu]
    else:
        gia_tri = int(ky_tu)
        
    trong_so = gia_tri * (2**i)
    tong_trong_so += trong_so

so_kiem_tra = tong_trong_so % 11

if so_kiem_tra == 10:
    so_kiem_tra = 0

print(f"Tổng các trọng số: {tong_trong_so}")
print(f"Số kiểm tra của mã container {container} là: {so_kiem_tra}")