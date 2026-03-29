
#Bai 1
#a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Kết quả:", tong)

#b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Kết quả:", tong)

#Bai 2
for i in range(1, 10):        
    for j in range(1, 10):
        print(f"{j}x{i}={i*j}", end="\t")
    print()

#Bài 3
n = int(input("Nhập số hàng: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Bài 4
import math
while True:
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Nhập lại!")

#a
S1 = 0
for i in range(1, n + 1):
    S1 += i

#b
S2 = 0
for i in range(1, n + 1):
    S2 += 1 / i

#c
S3 = 0
for i in range(1, n + 1):
    S3 += 1 / math.sqrt(2 * i)

#d
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1) ** (i + 1)) / i
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)

#Bài 5
for i in range(1, 1001):
    if int(i ** 0.5) ** 2 == i:
        print(i)

#Bài 6
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S += 1 / i
print("S =", S)

#Bài 7
n = int(input("Nhập n: "))
count = 0
for i in range(1, n + 1):
    tong = sum(int(d) for d in str(i))
    if tong % 2 == 0:
        count += 1
print("Số lượng:", count)

#Bài 8
n = int(input("Nhập n: "))
max_sum = 0
so = 0
for i in range(1, n + 1):
    tong = sum(int(d) for d in str(i))
    if tong > max_sum:
        max_sum = tong
        so = i
print("Số có tổng chữ số lớn nhất:", so)
print("Tổng chữ số:", max_sum)

#Bài 9
n = int(input("Nhập n: "))
max_uoc = 0
so = 0
for i in range(1, n + 1):
    dem = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem += 1
    if dem > max_uoc:
        max_uoc = dem
        so = i
print("Số có nhiều ước nhất:", so)
print("Số lượng ước:", max_uoc)

#Bài 11
n = int(input("Nhập số lượng fibonacci: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Bài 12
m = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,'J':20,
    'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,'S':30,'T':31,
    'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38
}
n = input("Nhập mã container (10 ký tự): ")
tong = 0
for i in range(len(n)):
    ky_tu = n[i]
    if ky_tu.isalpha():
        v = m[ky_tu]
    else:
        v = int(ky_tu)
    w = v * (2 ** i)
    tong += w
check_digit = tong % 11
if check_digit == 10:
    check_digit = 0
print("Tổng trọng số:", tong)
print("Số kiểm tra:", check_digit)
