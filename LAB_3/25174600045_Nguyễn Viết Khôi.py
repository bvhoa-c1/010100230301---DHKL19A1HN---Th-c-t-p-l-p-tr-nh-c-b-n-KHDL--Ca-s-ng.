#Bai 1a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng (chia hết cho 7, không chia hết cho 5):", tong)
#Bai 1b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng (chia hết cho 4, không chia hết cho 6):", tong)
#Bai 2
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:5}", end="")
    print()
#Bai 3
n = int(input("Nhập số hàng: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#Bai 4
import math
while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
    print("Nhập lại!")
#a
S1 = 0
for i in range(1, n + 1):
    S1 += i
#b
S2 = 0
for i in range(1, n + 1):
    S2 += 1 / i
#c
S3 = 0
for i in range(1, n + 1):
    S3 += 1 / math.sqrt(2 * i)
#d
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1) ** (i + 1)) / i
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
#Bai 5
import math
for i in range(1, 1001):
    if math.isqrt(i) ** 2 == i:
        print(i, end=" ")
#Bai 6
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S += 1 / i
print("Tổng S =", S)
#Bai 7
n = int(input("Nhập n: "))
dem = 0
for i in range(1, n + 1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong % 2 == 0:
        dem += 1
print("Số lượng số có tổng chữ số chẵn:", dem)
#Bai 8
n = int(input("Nhập n: "))
max_sum = 0
so_max = 0
for i in range(1, n + 1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong > max_sum:
        max_sum = tong
        so_max = i
print("Số có tổng chữ số lớn nhất:", so_max)
print("Tổng chữ số:", max_sum)
#Bai 9
n = int(input("Nhập n: "))
max_uoc = 0
so_max = 0
for i in range(1, n + 1):
    dem = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem += 1
    if dem > max_uoc:
        max_uoc = dem
        so_max = i
print("Số có nhiều ước nhất:", so_max)
print("Số lượng ước:", max_uoc)
#Bai 11
n = int(input("Nhập n: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#Bai 12
s = input("Nhập mã container (10 ký tự): ")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38]
tong = 0
for i in range(10):
    c = s[i]
    if 'A' <= c <= 'Z':
        for j in range(26):
            if c == letters[j]:
                v = values[j]
                break
    else:
        v = int(c)
    
    tong += v * (2 ** i)
check = tong % 11
if check == 10:
    check = 0
print("Số kiểm tra là:", check)
