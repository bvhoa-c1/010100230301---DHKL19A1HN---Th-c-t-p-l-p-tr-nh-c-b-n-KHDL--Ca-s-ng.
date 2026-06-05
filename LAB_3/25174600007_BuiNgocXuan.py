""" ---- BÀI TẬP VỀ NHÀ LAB 3 ----"""

""" Bài 1: a) Viết chương trình để tính tổng các số chia hết cho 7 nhưng không chia hết
cho 5 trong khoảng từ 2000 đến 4000.
b) Viết chương trình để tính tổng các số chia hết cho 4 nhưng không chia hết
cho 6 trong khoảng từ 500 đến 1000.
"""

#a
tong = 0

for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i

print("Tổng các số chia hết cho 7, không chia hết cho 5 là: ", tong)

#b
tong = 0

for j in range(500, 1001):
    if j % 4 == 0 and j % 6 != 0:
        tong += j

print("Tổng các số chia hết cho 4, không chia hết cho 6 là: ", tong)


""" Bài 2: In bảng cửu chương từ 1 đến 9 dạng bảng (2 chiều). """

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()


""" Bài 3: Vẽ tam giác vuông rỗng """

n = int(input("Nhập số hàng: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


""" Bài 4: Tính các tổng """

import math

while True:
    n = int(input("Nhập số nguyên dương n (bài 4): "))
    if n > 0:
        break
    else: 
        print("Yêu cầu nhập lại!")

#a
S1 = 0
for i in range(1, n + 1):
    S1 += i

print("S1 =", S1)

#b
S2 = 0
for i in range(1, n + 1):
    S2 += 1 / i

print("S2 =", S2)

#c
S3 = 0
for i in range(1, n + 1):
    S3 += 1 / math.sqrt(2 * i)

print("S3 =", S3)

#d
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1) ** (i + 1)) / i

print("S4 =", S4)


""" Bài 5: Tìm số chính phương. Sử dụng vòng lặp for để in ra tất cả các số chính
phương từ 1 đến 1000. Biết rằng số chính phương là số có căn bậc hai là một số
nguyên dương."""

for i in range(1, 32):  # vì 31**2 = 961 < 1000, 32**2 > 1000
    print(i * i, end=" ")


""" Bài 6: Viết chương trình tính tổng nghịch đảo của số nguyên đầu tiên: S1"""

while True:
    n = int(input("Nhập số nguyên n (bài 6): "))
    if n > 0:
        break
    else:
        print("Yêu cầu nhập lại!")

S1 = 0
for i in range(1, n + 1):
    S1 += 1 / i

print("Tổng S1 =", S1)


""" Bài 7: Nhập n. Đếm số lượng số trong khoảng [1, n] có tổng chữ số là số chẵn"""

n = int(input("Nhập số nguyên n (bài 7): "))
dem = 0

for i in range(1, n + 1):
    tong = 0
    
    for chu_so in str(i):
        tong += int(chu_so)
    
    if tong % 2 == 0:
        dem += 1

print("Tổng chữ số là số chẵn là:", dem)


""" Bài 8: Nhập n. Tìm số có tổng chữ số lớn nhất trong khoảng từ 1 đến n"""

n = int(input("Nhập số nguyên n (bài 8): "))
tong_max = 0
so_max = 0

for i in range(1, n + 1):
    tong = 0
    
    for chu_so in str(i):
        tong += int(chu_so)
    
    if tong > tong_max:
        tong_max = tong
        so_max = i
print("Số có tổng chữ số lớn nhất là:", so_max)
print("Tổng chữ số của số lớn nhất đó là:", tong_max)


""" Bài 9: Nhập n. Tìm số có nhiều ước nhất trong khoảng từ 1 đến n"""

n = int(input("Nhập số nguyên n (bài 9): "))
uoc_max = 0
so_max = 0

for i in range(1, n + 1):
    dem = 0
    
    for j in range(1, i + 1):
        if i % j == 0:
            dem += 1
    
    if dem > uoc_max:
        uoc_max = dem
        so_max = i
print("Số có nhiều ước nhất là:", so_max)
print("Số lượng ước là:", uoc_max)


""" Bài 11: In ra n số Fibonacci đầu tiên bằng vòng lặp for."""

n = int(input("Nhập số nguyên n (bài 11): "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


""" Bài 12: Viết chương trình tính số kiểm tra container (check digit), biết số container
chuẩn là một chuỗi 10 ký tự, trong đó 04 ký tự đầu tiên là chữ cái in hoa (A–Z)
được mã hóa thành số theo bảng sau (bỏ qua các số là bội số của 11):

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
10 12 13 14 15 16 17 18 19 20 21 23 24 25 26 27 28 29 30 31 32 34 35 36 37 38

Các ký tự số giữ nguyên giá trị.
"""

# Bảng mã chữ cái
bang_ma = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,'J':20,
    'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,'S':30,'T':31,
    'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38
}

container = input("Nhập mã container (10 kí tự): ")  #mã container gồm 10 kí tự
tong = 0

for i in range(10):
    ki_tu = container[i]
    
    # Nếu là chữ
    if ki_tu.isalpha():
        gia_tri = bang_ma[ki_tu]
    else:
        gia_tri = int(ki_tu)
    
    # Tính trọng số
    tong += gia_tri * (2 ** i)

# Tính số kiểm tra
check_digit = tong % 11

if check_digit == 10:
    check_digit = 0

print("Số kiểm tra của mã container là:", check_digit)








