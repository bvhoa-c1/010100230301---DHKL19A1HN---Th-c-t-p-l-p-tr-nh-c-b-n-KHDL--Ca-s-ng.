#bai1
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i

print("Tổng =",tong)
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i

print("Tổng =", tong)
#bai2
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:4}", end=" ")
    print()
#Bai 3
n = int(input("Nhập số hàng: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#bai4
import math

n = int(input("Nhập n (n > 10): "))

# ===== a) S1 = 6 + 6^2 + ... + 6^n =====
tong1 = 0
for i in range(1, n + 1):
    tong1 += 6 ** i

# ===== b) S2 = 1/3 + 1/3^3 + ... + 1/3^(2n+1) =====
tong2 = 0
for i in range(0, n + 1):
    tong2 += 1 / (3 ** (2*i + 1))

# ===== c) S3 = 1/sqrt(2) + 1/sqrt(4) + ... + 1/sqrt(2n) =====
tong3 = 0
for i in range(1, n + 1):
    tong3 += 1 / math.sqrt(2 * i)

# ===== d) S4 = 1*2*3 + 2*3*4 + ... + n(n+1)(n+2) =====
tong4 = 0
for i in range(1, n + 1):
    tong4 += i * (i + 1) * (i + 2)

# ===== In kết quả =====
print("S1 =", tong1)
print("S2 =", tong2)
print("S3 =", tong3)
print("S4 =", tong4)
# Bai 5
for i in range(1, 1001):
    if int(i**0.5)**2 == i:
        print(i, end=" ")
# Bai 6
n = int(input("Nhập n: "))
tong = 0

for i in range(1, n + 1):
    tong += 1 / i

print("S =", tong)
#Bai 7
n = int(input("Nhập n: "))
dem = 0

for i in range(1, n + 1):
    s = sum(int(d) for d in str(i))
    if s % 2 == 0:
        dem += 1

print("Số lượng =", dem)
#Bai 8
n = int(input("Nhập n: "))
max_sum = 0
so_max = 0

for i in range(1, n + 1):
    s = sum(int(d) for d in str(i))
    if s > max_sum:
        max_sum = s
        so_max = i

print("Số =", so_max)
print("Tổng chữ số =", max_sum)
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

print("Số =", so_max)
print("Số ước =", max_uoc)
# Bai 11
n = int(input("Nhập n: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#Bai 12
# Bảng mã ký tự
bang = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,'J':20,
    'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,'S':30,'T':31,
    'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38
}

container = input("Nhập mã container (10 ký tự): ")

tong = 0

for i in range(10):
    kytu = container[i]

    if kytu.isalpha():
        giatri = bang[kytu]
    else:
        giatri = int(kytu)

    tong += giatri * (2 ** i)

check_digit = tong % 11
if check_digit == 10:
    check_digit = 0

print("Check digit =", check_digit)
