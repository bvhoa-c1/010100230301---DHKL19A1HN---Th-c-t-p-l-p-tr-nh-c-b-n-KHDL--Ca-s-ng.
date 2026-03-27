# Bài 1
# a
tong_1a = sum(i for i in range(2000, 4001) if i % 7 == 0 and i % 5 != 0)
print(tong_1a)

# b
tong_1b = sum(i for i in range(500, 1001) if i % 4 == 0 and i % 6 != 0)
print(tong_1b)

# Bài 2
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} x {i} = {i*j:2d}", end="\t")
    print()

# Bài 3
n = int(input("Nhập số hàng: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Bài 5
for i in range(1, 1001):
    can = i**0.5
    if can == int(can):
        print(i, end=" ")
print()

# Bài 6
n = int(input("Nhập n: "))
s1 = sum(1/i for i in range(1, n + 1))
print(s1)

# Bài 7
n = int(input("Nhập n: "))
dem = 0
for i in range(1, n + 1):
    tong_cs = sum(int(d) for d in str(i))
    if tong_cs % 2 == 0:
        dem += 1
print(dem)

# Bài 8
n = int(input("Nhập n: "))
max_tong = -1
so_tim_duoc = 0
for i in range(1, n + 1):
    tong_cs = sum(int(d) for d in str(i))
    if tong_cs > max_tong:
        max_tong = tong_cs
        so_tim_duoc = i
print(so_tim_duoc)

# Bài 9
n = int(input("Nhập n: "))
max_uoc = 0
so_nhieu_uoc = 0
for i in range(1, n + 1):
    dem_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_nhieu_uoc = i
print(so_nhieu_uoc)

# Bài 11
n = int(input("Nhập n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Bài 12
container = input("Nhập mã container (10 ký tự): ")
ma_chu = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

tong_trong_so = 0
for i in range(10):
    ky_tu = container[i].upper()
    if ky_tu.isalpha():
        gia_tri = ma_chu[ky_tu]
    else:
        gia_tri = int(ky_tu)
    tong_trong_so += gia_tri * (2**i)

so_kiem_tra = tong_trong_so % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0
print(so_kiem_tra)