# Bài 1:
# a
tong = 0
for i in range(2000,4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng là: ", tong)
# b
tong = 0
for i in range(500,10010):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng là:", tong)
# Bài 2:
for i in range(1, 10):
    for j in range(1,10):
        print(f"{i*j:4}", end="")
    print()
# Bài 3:
n = int(input("Nhập số hàng:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Bài 4:
while True:
    n = int(input("Nhập n:"))
    if n > 0:
        break
# a
S1 = 0
for i in range(1, n+1):
    S1 += i
print("S1= ", S1)
# b
S2 = 0
for i in range(1, n+1):
    S2 += 1/i
print("S2=", S2)
#c
import math
S3 = 0
for i in range(1, n+1):
    S3 += 1/ math.sqrt(2*i)
print("S3=", S3)
#d
S4 = 0
for i in range(1, n+1):
    S4 += ((-1) ** (i + 1)) / i
print("S4=", S4)
# BÀi 5
while True:
    n = int(input("Nhập n:"))
    if n > 0:
        break
for i in range(1, 1001):
    if int(i**0.5)**2 == i:
        print(i, end=" ")
# Bài 6:
n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1):
    tong += 1/i
print("Tổng S=", tong)
# Bài 7:
n = int(input("Nhập n:"))
dem = 0
for i in range(1, n+1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong % 2 == 0:
        dem += 1
print("Số lượng: ", dem)
# BÀi 8:
n = int(input("Nhập n: "))
max_tong = 0
so = 0
for i in range(1, n+1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong > max_tong:
        max_tong = tong
        so = i
print("Số cần tìm:", so)
# Bài 9:
n = int(input("Nhấp n:"))
max_uoc = 0
so = 0
for i in range(1, n+1):
    dem = 0
    for j in range(1, i+1):
        if i % j == 0:
            dem += 1
    if dem > max_uoc:
        max_uoc = dem
        so = i
print("Số có nhiều ước nhất:", so)
# Bài 11:
n = int(input("Nhập n:"))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# Bài 12:
container = input("Nhấp mã container ( 10 kí tự)")
bang = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,'J':20,
    'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,'S':30,'T':31,
    'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38
}
tong = 0
for i in range(len(container)):
    ky_tu = container[i]
    if ky_tu in bang:
        gia_tri = bang[ky_tu]
    else:
        gia_tri = int(ky_tu)
    trong_so = gia_tri * (2**i)
    tong = tong + trong_so
ket_qua = tong % 11
if ket_qua == 10:
    ket_qua = 0
print("Số kiểm tra là: ", ket_qua)