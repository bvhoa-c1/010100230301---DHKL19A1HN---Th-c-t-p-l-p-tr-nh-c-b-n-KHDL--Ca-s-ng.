#bai 1
print("bai 1")
tong_a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong_a += i
print(tong_a)
tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print(tong_b)
#bai 2
print("bai 2")
for i in range(1, 11):
    for j in range(1, 10):
        print(f"{j}x{i}={i*j}", end="\t")
    print()
#bai 3
print("bai 3")
n = int(input("nhap so hang: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#bai 4
print("bai 4")
n = 0
while n <= 0:
    n = int(input("Nhập n: "))

s1 = s2 = s3 = s4 = 0
for i in range(1, n + 1):
    s1 += i
    s2 += 1/i
    s3 += 1/((2*i)**0.5)
    s4 += ((-1)**(i+1)) / i

print(s1)
print(s2)
print(s3)
print(s4)
#bai 5
print("bai 5")
for i in range(1, 1001):
    if (i**0.5) == int(i**0.5):
        print(i)
#bai 6
print("bai 6")
n = int(input("nhap n: "))
s1 = 0
for i in range(1, n + 1):
    s1 += 1/i
print(s1)
#bai 7
print("bai 7")
n = int(input("nhap n: "))
dem = 0
for i in range(1, n + 1):
    tong_cs = 0
    for chu_so in str(i):
        tong_cs += int(chu_so)
    if tong_cs % 2 == 0:
        dem += 1
print(dem)
#bai 8
print("bai 8")
def new_func():
    n = int(input("nhap n: "))
    return n

n = new_func()
max_t = -1
ket_qua = 0
for i in range(1, n + 1):
    tong_i = 0
    for c in str(i):
        tong_i += int(c)
    if tong_i > max_t:
        max_t = tong_i
        ket_qua = i
print(ket_qua)
#bai 9
print("bai 9")
n = int(input("nhap n: "))
so_nhieu_uoc_nhat = 0
so_luong_uoc_lon_nhat = 0

for i in range(1, n + 1):
    dem_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    
    if dem_uoc > so_luong_uoc_lon_nhat:
        so_luong_uoc_lon_nhat = dem_uoc
        so_nhieu_uoc_nhat = i

print(so_nhieu_uoc_nhat)
#bai 11
print("bai 11")
n = int(input("nhap n: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
#bai 12
print("bai 12")
ma_container = input("Nhap ma container: ").upper()
chu_cai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bang_ma_so = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38]

tong_trong_so = 0
for vi_tri in range(10):
    ky_tu = ma_container[vi_tri]
    if 'A' <= ky_tu <= 'Z':
        vi_tri_chu = chu_cai.find(ky_tu)
        gia_tri_quy_doi = bang_ma_so[vi_tri_chu]
    else:
        gia_tri_quy_doi = int(ky_tu)
    
    trong_so = gia_tri_quy_doi * (2**vi_tri)
    tong_trong_so += trong_so

so_kiem_tra = tong_trong_so % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0

print(so_kiem_tra)
