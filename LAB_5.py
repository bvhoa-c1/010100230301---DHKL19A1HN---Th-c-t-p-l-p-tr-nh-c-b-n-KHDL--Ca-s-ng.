#LAB_5

#Bài 5.1
n = int(input("Nhap so nguyen duong: "))
print("Nhi phan:", bin(n)[2:])


#Bài 5.2
str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

ket_qua = ""
for c in str1:
    if c in str2:
        ket_qua = c
        break

if ket_qua:
    print("Chuoi con chung ngan nhat:", ket_qua)
else:
    print("Khong co chuoi con chung")


#Bài 5.3
chuoi = input("Nhap chuoi van ban: ")
tu_khoa = input("Nhap tu khoa: ")

vi_tri = []
for i in range(len(chuoi)):
    if chuoi.startswith(tu_khoa, i):
        vi_tri.append(i)

print("Vi tri xuat hien:", vi_tri)

tu = chuoi.lower().split()
dem = {}
for x in tu:
    x = x.strip(".,!?;:")
    dem[x] = dem.get(x, 0) + 1

max_tu = max(dem, key=dem.get)
print("Tu xuat hien nhieu nhat:", max_tu, "-", dem[max_tu], "lan")


#Bài 5.4
s = input("Nhap xau: ")

so = ""
for c in s:
    if c.isdigit():
        so += c

if so == "":
    print("Khong co chu so")
else:
    n = int(so)
    la_nguyen_to = True

    if n < 2:
        la_nguyen_to = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                la_nguyen_to = False
                break

    print("So sau khi loc:", n)
    if la_nguyen_to:
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")


#Bài 5.5
a = input("Nhap chuoi 1: ")
b = input("Nhap chuoi 2: ")

kq = []
for i in range(max(len(a), len(b))):
    if i < len(a):
        kq.append(a[i])
    if i < len(b):
        kq.append(b[i])

print("-".join(kq))


#Bài 5.6
s = input("Nhap xau: ")

dem = {}
for c in s:
    if not c.isalnum():
        dem[c] = dem.get(c, 0) + 1

for c in dem:
    print(c, ":", dem[c], "lan,", round(dem[c] / len(s) * 100, 2), "%")


#Bài 5.7
s = input("Nhap xau: ")

thuong = hoa = so = dac_biet = 0

for c in s:
    if c.islower():
        thuong += 1
    elif c.isupper():
        hoa += 1
    elif c.isdigit():
        so += 1
    else:
        dac_biet += 1

print("Chu thuong:", thuong)
print("Chu hoa:", hoa)
print("Chu so:", so)
print("Ky tu dac biet:", dac_biet)


#Bài 5.8
s = input("Nhap xau dai hon 10 ky tu: ")

if len(s) <= 10:
    print("Xau phai dai hon 10 ky tu")
else:
    print("Tu vi tri 2 den 8:", s[2:9])
    print("5 ky tu tu vi tri 5:", s[5:10])
    print("3 ky tu cuoi:", s[-3:])
    print("In hoa:", s.upper())
    print("In thuong:", s.lower())
    print("Dao nguoc:", s[::-1])


#Bài 5.9
s1 = input("Nhap chuoi ban dau: ")
s2 = input("Nhap chuoi muc tieu: ")

m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            cost = 0
        else:
            cost = 1

        dp[i][j] = min(
            dp[i - 1][j] + 1,
            dp[i][j - 1] + 1,
            dp[i - 1][j - 1] + cost
        )

print("So thao tac it nhat:", dp[m][n])


#Bài 5.10
s = input("Nhap xau: ")
s = s.replace(" ", "")
print("Xau sau khi xoa khoang trang:", s)