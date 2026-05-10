# Bài 8.1
# Số nguyên tố sinh đôi

def so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

for i in range(2, 1000):
    if so_nguyen_to(i) and so_nguyen_to(i + 2):
        print((i, i + 2))

# Bài 8.2
# Hàm giai thừa

def giaithua(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt

n = int(input("Nhập n: "))

print("Giai thừa =", giaithua(n))

# Bài 8.3
# Hoán vị và tổ hợp

def giaithua(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt

def hoanvi(n, r):
    return giaithua(n) // giaithua(n - r)

def tohop(n, r):
    return giaithua(n) // (giaithua(r) * giaithua(n - r))

n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

print("Hoán vị =", hoanvi(n, r))
print("Tổ hợp =", tohop(n, r))

# Bài 8.4
# cubesum

def cubesum(n):
    tong = 0

    for i in str(n):
        tong += int(i) ** 3

    return tong

n = int(input("Nhập số: "))

print("Cube sum =", cubesum(n))

# Bài 8.5
# Số Armstrong

def cubesum(n):
    tong = 0

    for i in str(n):
        tong += int(i) ** 3

    return tong

def isArmstrong(n):
    return cubesum(n) == n

print("Các số Armstrong:")

for i in range(1000):
    if isArmstrong(i):
        print(i)

# Bài 8.6
# Tổng ước thực sự

def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong

n = int(input("Nhập số: "))

print("Tổng ước =", sumPdivisors(n))

# Bài 8.7
# Số amicable

def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong

def amicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if amicable(a, b):
    print("Là cặp amicable")
else:
    print("Không phải")    

# Bài 8.8
# filter và lambda

a = [1, 2, 3, 4, 5, 6]

chan = list(filter(lambda x: x % 2 == 0, a))
le = list(filter(lambda x: x % 2 != 0, a))

print("Số chẵn:", chan)
print("Số lẻ:", le)

# Bài 8.9
# map lập phương

a = [1, 2, 3, 4, 5]

lap_phuong = list(map(lambda x: x**3, a))

print(lap_phuong)

# Bài 8.10
# map + filter

a = [1, 2, 3, 4, 5, 6]

chan = list(map(lambda x: x**3,
                filter(lambda x: x % 2 == 0, a)))

le = list(map(lambda x: x**2,
              filter(lambda x: x % 2 != 0, a)))

print("Lập phương số chẵn:", chan)
print("Bình phương số lẻ:", le)

