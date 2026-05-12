#Bài 8.1:
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Các cặp số nguyên tố sinh đôi nhỏ hơn 1000:")
for i in range(2, 1000):
    if la_nguyen_to(i) and la_nguyen_to(i + 2):
        print(i, "và", i + 2)

#Bài 8.2:
def giai_thua(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua
n = int(input("Nhập số nguyên dương: "))
print("Giai thừa là:", giai_thua(n))

#Bài 8.3:
def giai_thua(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua
def hoan_vi(n, r):
    return giai_thua(n) // giai_thua(n - r)
def to_hop(n, r):
    return giai_thua(n) // (giai_thua(r) * giai_thua(n - r))
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
print("Hoán vị:", hoan_vi(n, r))
print("Tổ hợp:", to_hop(n, r))

#Bài 8.4:
def cubesum(n):
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so) ** 3
    return tong
n = int(input("Nhập số: "))
print("Tổng lập phương các chữ số là:")
print(cubesum(n))

#Bài 8.5:
def cubesum(n):
    tong = 0
    for chu_so in str(n): 
        tong += int(chu_so) ** 3
    return tong
def isArmstrong(n):
    return cubesum(n) == n
print("Các số Armstrong nhỏ hơn 1000:")
for i in range(1000):
    if isArmstrong(i):
        print(i)

#Bài 8.6:
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
n = int(input("Nhập số: "))
print("Tổng các ước số thực sự là:")
print(sumPdivisors(n))

#Bài 8.7:
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
def la_amicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if la_amicable(a, b):
    print("Đây là cặp số Amicable")
else:
    print("Không phải cặp số Amicable")

#Bài 8.8:
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9]
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
so_le = list(filter(lambda x: x % 2 != 0, danh_sach))
print("Danh sách số chẵn:")
print(so_chan)
print("Danh sách số lẻ:")
print(so_le)

#Bài 8.9:
danh_sach = [1, 2, 3, 4, 5]
lap_phuong = list(map(lambda x: x ** 3, danh_sach))
print("Danh sách lập phương:")
print(lap_phuong)

#Bài 8.10:
danh_sach = [1, 2, 3, 4, 5, 6]
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
so_le = list(filter(lambda x: x % 2 != 0, danh_sach))
lap_phuong_chan = list(map(lambda x: x ** 3, so_chan))
binh_phuong_le = list(map(lambda x: x ** 2, so_le))
print("Lập phương các số chẵn:")
print(lap_phuong_chan)
print("Bình phương các số lẻ:")
print(binh_phuong_le)