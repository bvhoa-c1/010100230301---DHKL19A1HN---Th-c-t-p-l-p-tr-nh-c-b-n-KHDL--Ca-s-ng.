#bai 1
# a
"""tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print(" tổng la:", tong)
#b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print(" tổng la:", tong)

# bai 2
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:4}", end="")

# bai 3
n = int(input("nhập số hàng:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print("", end="")
    print()

# bai 4
while True:
    n = int(input("nhập n > 0:"))
    if n > 0:
        break
#a
S1 = 0
for i in range(1, n + 1):
    S1 += i

print("S1 =", S1)

#b
S2 = 0
for i in range(1, n + 1):
    S2 += 1/i
print("S2=", S2)

#c
import math

S3 = 0
for i in range(1, n + 1):
    S3 += 1 / math.sqrt(2 * i)

print("S3 =", S3)

#s
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1) ** (i + 1)) / i

print("S4 =", S4)

# bài 5
import math

for i in range(1, 1001):
    if int(math.sqrt(i)) ** 2 == i:
        print(i, end=" ")

# bai 6
n = int(input("Nhập n: "))

S1 = 0
for i in range(1, n + 1):
    S1 += 1 / i

print("S1 =", S1)

# bai 7
n = int(input(" nhập n :"))
dem = 0
for i in range(1, n + 1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong % 2== 0:
        dem += 1
print(" số lượng =", dem)


# bai 8
n = int(input("nhập n:"))
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
print(" số có tổng chữ số lớn nhất:", so_max)

# bai 9
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
n = int(input("nhập n :"))
a, b = 0, 1
for i in range(n):
    print(a, end ="")
    a, b= b, a+b"""

# bài 12
# bảng mã chữ
bang = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,
    'J':20,'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,
    'S':30,'T':31,'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38
}

container = input("Nhập mã container (10 ký tự): ").upper()

tong = 0

for i in range(len(container)):
    kytu = container[i]
    
    # đổi ký tự thành số
    if kytu.isalpha():
        value = bang[kytu]
    else:
        value = int(kytu)
    
    # nhân với 2^i
    tong += value * (2 ** i)

# tính check digit
check = tong % 11

if check == 10:
    check = 0

print("Check digit =", check)






