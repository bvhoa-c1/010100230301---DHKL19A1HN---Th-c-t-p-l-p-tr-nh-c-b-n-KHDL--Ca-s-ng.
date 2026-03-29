# a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng a =", tong)

# b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng b =", tong)
# bài 2
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print()
#bai 3
n = int(input("Nhập số hàng: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#bài 4
import math

n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (>0): "))

S1 = 0
S2 = 0
S3 = 0
S4 = 0

for i in range(1, n+1):
    S1 = S1 + i
    S2 = S2 + 1/i
    S3 = S3 + 1/math.sqrt(2*i)
    S4 = S4 + ((-1)**(i+1))/i

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
# bai 5
for i in range(1, 1001):
    if int(i**0.5) ** 2 == i:
        print(i, end=" ")
# bài 6
n = int(input("Nhập n: "))
tong = 0

for i in range(1, n + 1):
    tong += 1 / i

print("Tổng =", tong)
#bai 7
n = int(input("Nhập n: "))
dem = 0

for i in range(1, n + 1):
    x = i
    tong = 0
    
    while x > 0:
        tong += x % 10
        x //= 10
    
    if tong % 2 == 0:
        dem += 1

print("Số lượng:", dem)
#bài 8
n = int(input("Nhập n: "))

max_sum = 0
so_max = 0

for i in range(1, n + 1):
    x = i
    tong = 0
    
    while x > 0:
        tong += x % 10
        x //= 10
    
    if tong > max_sum:
        max_sum = tong
        so_max = i

print("Số cần tìm:", so_max)
# bài 9
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
# bài 11
n = int(input("Nhập n: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# bài 12
container = input("Nhập mã: ")
tong = 0

for i in range(len(container)):
    k = container[i]
    
    if k == 'A': value = 10
    elif k == 'B': value = 12
    elif k == 'C': value = 13
    elif k == 'D': value = 14
    elif k == 'E': value = 15
    elif k == 'F': value = 16
    elif k == 'G': value = 17
    elif k == 'H': value = 18
    elif k == 'I': value = 19
    elif k == 'J': value = 20
    elif k == 'K': value = 21
    elif k == 'L': value = 23
    elif k == 'M': value = 24
    elif k == 'N': value = 25
    elif k == 'O': value = 26
    elif k == 'P': value = 27
    elif k == 'Q': value = 28
    elif k == 'R': value = 29
    elif k == 'S': value = 30
    elif k == 'T': value = 31
    elif k == 'U': value = 32
    elif k == 'V': value = 34
    elif k == 'W': value = 35
    elif k == 'X': value = 36
    elif k == 'Y': value = 37
    elif k == 'Z': value = 38
    else:
        value = int(k)  # nếu là số

    tong += value * (2 ** i)

check = tong % 11
if check == 10:
    check = 0

print("Check digit =", check)