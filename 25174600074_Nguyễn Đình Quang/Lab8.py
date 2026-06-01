# Bài 8.1
import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

for i in range(2, 998):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i + 2})", end=", ")
# Bài 8.2
def giai_thua(n):
    if n == 0 or n == 1: return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua

n = int(input("Nhập số nguyên dương n: "))
print(f"{n}! = {giai_thua(n)}")
# Bài 8.3
def giai_thua(n):
    if n == 0 or n == 1: return 1
    ket_qua = 1
    for i in range(2, n + 1): ket_qua *= i
    return ket_qua

def hoan_vi(n, r):
    if r > n or n < 0 or r < 0: return 0
    return giai_thua(n) // giai_thua(n - r)

def to_hop(n, r):
    if r > n or n < 0 or r < 0: return 0
    return giai_thua(n) // (giai_thua(r) * giai_thua(n - r))

n, r = int(input("Nhập n: ")), int(input("Nhập r: "))
print(f"Hoán vị P({n},{r}) = {hoan_vi(n, r)}")
print(f"Tổ hợp C({n},{r}) = {to_hop(n, r)}")
# Bài 8.4
def cubesum(n):
    tong = 0
    while n > 0:
        tong += (n % 10) ** 3
        n //= 10
    return tong

so = int(input("Nhập số nguyên: "))
print(f"Tổng các lập phương chữ số: {cubesum(so)}")
# Bài 8.5
def cubesum(n):
    tong, temp = 0, n
    while temp > 0:
        tong += (temp % 10) ** 3
        temp //= 10
    return tong

def isArmstrong(n):
    return cubesum(n) == n

armstrong_list = [x for x in range(1, 1001) if isArmstrong(x)]
print(f"Các số Armstrong: {armstrong_list}")
# Bài 8.6
def sumPDivisors(n):
    if n <= 1: return 0
    tong_uoc = 1 
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc

so = int(input("Nhập số nguyên dương: "))
print(f"Tổng các ước thực sự: {sumPDivisors(so)}")
# Bài 8.7
def sumPDivisors(n):
    if n <= 1: return 0
    tong_uoc = 1 
    for i in range(2, (n // 2) + 1):
        if n % i == 0: tong_uoc += i
    return tong_uoc

def is_amicable(a, b):
    return sumPDivisors(a) == b and sumPDivisors(b) == a

so_1, so_2 = 220, 284
print(f"({so_1}, {so_2}) là số Amicable? -> {is_amicable(so_1, so_2)}")
# Bài 8.8
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nhom_chan = list(filter(lambda x: x % 2 == 0, arr))
nhom_le = list(filter(lambda x: x % 2 != 0, arr))

print(f"Nhóm chẵn: {nhom_chan}")
print(f"Nhóm lẻ: {nhom_le}")
# Bài 8.9
arr = [1, 2, 3, 4, 5]

lap_phuong = list(map(lambda x: x**3, arr))
print(f"Giá trị lập phương: {lap_phuong}")
# Bài 8.10
arr = [1, 2, 3, 4, 5, 6]

chan_lap_phuong = list(map(lambda x: x**3, filter(lambda x: x % 2 == 0, arr)))
le_binh_phuong = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, arr)))

print(f"Số chẵn lập phương: {chan_lap_phuong}")
print(f"Số lẻ bình phương: {le_binh_phuong}")