
# Bài 8.1
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Các cặp số nguyên tố sinh đôi nhỏ hơn 1000:")
for i in range(2, 1000):
    if kiem_tra_so_nguyen_to(i) and kiem_tra_so_nguyen_to(i + 2):
        print(i, "và", i + 2)
 # Bài 8.2
def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua
n = int(input("Nhập n: "))
print("Giai thừa là:", tinh_giai_thua(n))
# Bài 8.3
def tinh_giai_thua(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua
def tinh_hoan_vi(n, r):
    return tinh_giai_thua(n) / tinh_giai_thua(n - r)
def tinh_to_hop(n, r):
    return tinh_giai_thua(n) / (
        tinh_giai_thua(r) * tinh_giai_thua(n - r)
    )
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
print("Hoán vị là:", tinh_hoan_vi(n, r))
print("Tổ hợp là:", tinh_to_hop(n, r))
# bài 8.4:
def cubesum(n):
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so) ** 3
    return tong
n = int(input("Nhập số: "))
print("Tổng lập phương là:", cubesum(n))
# Bài 8.5
def cubesum(n):
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so) ** 3
    return tong
def isArmstrong(n):
    return cubesum(n) == n
print("Các số Armstrong từ 1 đến 1000 là:")
for i in range(1, 1001):
    if isArmstrong(i):
        print(i)
# Bài 8.6
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
n = int(input("Nhập số: "))
print("Tổng các ước số thực sự là:", sumPdivisors(n))
# Bài 8.7:
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
def kiem_tra_amicable(a, b):
    if sumPdivisors(a) == b and sumPdivisors(b) == a:
        return True
    return False
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if kiem_tra_amicable(a, b):
    print("Đây là cặp số Amicable")
else:
    print("Đây không phải cặp số Amicable")
# bÀI 8.8
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8]
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
so_le = list(filter(lambda x: x % 2 != 0, danh_sach))
print("Danh sách số chẵn:")
print(so_chan)
print("Danh sách số lẻ:")
print(so_le)
#Bài 8.9
danh_sach = [1, 2, 3, 4, 5]
lap_phuong = list(map(lambda x: x ** 3, danh_sach))
print("Danh sách lập phương là:")
print(lap_phuong)
# Bài 8.10
danh_sach = [1, 2, 3, 4, 5, 6]
ket_qua = list(
    map(
        lambda x: x * 3 if x % 2 == 0 else x * 2,
        danh_sach
    )
)
print("Kết quả là:")
print(ket_qua)

