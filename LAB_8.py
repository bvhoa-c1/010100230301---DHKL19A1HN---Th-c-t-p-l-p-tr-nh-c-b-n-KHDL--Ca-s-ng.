#Bài 8.1
cap_sinh_doi = []

for x in range(2, 999):
    nt1 = True
    if x < 2:
        nt1 = False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                nt1 = False
                break

    y = x + 2
    nt2 = True
    if y < 2:
        nt2 = False
    else:
        for i in range(2, int(y ** 0.5) + 1):
            if y % i == 0:
                nt2 = False
                break

    if nt1 and nt2:
        cap_sinh_doi.append((x, y))

print("Cac cap so nguyen to sinh doi nho hon 1000:")
print(cap_sinh_doi)


#Bài 8.2
n = int(input("Nhap n: "))

gt = 1
for i in range(1, n + 1):
    gt *= i

print("Giai thua:", gt)


#Bài 8.3
n = int(input("Nhap n: "))
r = int(input("Nhap r: "))

gt_n = 1
for i in range(1, n + 1):
    gt_n *= i

gt_r = 1
for i in range(1, r + 1):
    gt_r *= i

gt_nr = 1
for i in range(1, n - r + 1):
    gt_nr *= i

P = gt_n // gt_nr
C = gt_n // (gt_r * gt_nr)

print("Hoan vi chap r:", P)
print("To hop chap r:", C)


#Bài 8.4
n = int(input("Nhap n: "))
tam = abs(n)
tong = 0

while tam > 0:
    cs = tam % 10
    tong += cs ** 3
    tam //= 10

print("Tong lap phuong cac chu so:", tong)


#Bài 8.5
n = int(input("In cac so Armstrong tu 0 den n = "))

ds = []

for x in range(n + 1):
    tam = x
    tong = 0

    if tam == 0:
        tong = 0

    while tam > 0:
        cs = tam % 10
        tong += cs ** 3
        tam //= 10

    if tong == x:
        ds.append(x)

print("Cac so Armstrong:", ds)


#Bài 8.6
n = int(input("Nhap n: "))

tong = 0
for i in range(1, n):
    if n % i == 0:
        tong += i

print("Tong uoc so thuc su:", tong)


#Bài 8.7
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

tong_a = 0
for i in range(1, a):
    if a % i == 0:
        tong_a += i

tong_b = 0
for i in range(1, b):
    if b % i == 0:
        tong_b += i

if tong_a == b and tong_b == a:
    print("La cap so Amicable")
else:
    print("Khong phai cap so Amicable")


#Bài 8.8
a = list(map(int, input("Nhap mang: ").split()))

chan = list(filter(lambda x: x % 2 == 0, a))
le = list(filter(lambda x: x % 2 != 0, a))

print("So chan:", chan)
print("So le:", le)


#Bài 8.9
a = list(map(int, input("Nhap mang: ").split()))

lap_phuong = list(map(lambda x: x ** 3, a))

print("Danh sach lap phuong:", lap_phuong)


#Bài 8.10
a = list(map(int, input("Nhap mang: ").split()))

lap_phuong_chan = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, a)))
binh_phuong_le = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, a)))

print("Lap phuong so chan:", lap_phuong_chan)
print("Binh phuong so le:", binh_phuong_le)
