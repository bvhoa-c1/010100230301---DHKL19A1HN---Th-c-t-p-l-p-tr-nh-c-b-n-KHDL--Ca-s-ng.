#bai 1
# ý a
s1 = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0 :
        s1 = s1 + i 
print(s1)

# ý b
S2 = 0 
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0 :
        S2 = S2 + i
print(S2)

# bài 2
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j , "=", i*j)
    print()

# bai 3 
n = int(input("nhập vào số hàng: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or j == n :
            print("*", end = " ")
        else :
            print(" ", end = " ")
    print()


# bài 4 
import math
n = int(input("nhập vào số nguyên dương n : "))
if  n <= 0 :
    print("sai , yêu cầu nhập lại")
else :
    # ý 1 
    S1 = 0
    for i in range(1, n):
        S1 = S1 + i
    print(S1)

    # ý 2
    S2 = 0
    for i in range(1, n+1):
        S2 += 1/i
    print(S2)

    # ý 3
    S3 = 0 
    for i in range(1, n+1):
        S3 += 1/math.sqrt(2*i)
    print(S3)


    # ý 4
    S4 = 0
    for i in range(1, n+1):
        S4 += ((-1)**(i+1))/i
    print(S4)

# bài 5 :
import math
print("\n Các số chính phương từ 1 đến 1000 là : ")
for i in range(1, 1001):
    can = math.sqrt(i)
    if int(can) == can :
        print(i, end = " ")
print()


# bài 6 :
n = int(input("nhập n : "))
S = 0
for i in range(1, n+1):
    S += 1/i
print(S)


# bài 7 
n = int(input("Nhập n : "))
dem = 0
for i in range(1, n+1):
    tong_chu_so = 0
    for chu_so in str(i):
        tong_chu_so += int(chu_so)
    if tong_chu_so % 2 == 0 :
        dem = dem + 1
print(f"Có {dem} số trong khoảng [1, {n}] có tổng chữ số là số chẵn ")

# bài 8 :
max_tong = 0
so_cantim = 1
for i in range(1, n+1):
    tong_chu_so = 0
    for chu_so in str(i):
        tong_chu_so += int(chu_so)
    if tong_chu_so > max_tong :
        max_tong = tong_chu_so 
        so_cantim = i
print(f"Số có tổng chữ số lớn nhất là {so_cantim} (tổng các chữ số = {max_tong})")

# bài 9 
n = int(input("Nhập n: "))
max_uoc = 0
so_nhieu_uoc_nhat = 1
for i in range(1, n + 1):
    dem_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_nhieu_uoc_nhat = i

print(f"Số có nhiều ước nhất là {so_nhieu_uoc_nhat} (có {max_uoc} ước)")

# bài 11 :
n = int(input("Nhập số lượng số Fibonacci cần in (n > 0): "))
f0 = 0
f1 = 1
print(f"{n} số Fibonacci đầu tiên là: ", end="")
for i in range(n):
    if i == 0:
        print(f0, end=" ")
    elif i == 1:
        print(f1, end=" ")
    else:
        fn = f0 + f1
        print(fn, end=" ")
        f0 = f1
        f1 = fn

# bài 12 :
bang_ma = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17,
    'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25,
    'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32,
    'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

# Yêu cầu người dùng nhập chuỗi 10 ký tự. Hàm .upper() giúp viết hoa mọi chữ cái.
container = input("Nhập mã container (10 ký tự, VD: SUDU307007): ").upper()
tong_trong_so = 0
for a in range(10):
    ky_tu = container[a]   
    # Lấy giá trị của ký tự
    if ky_tu.isalpha(): # Nếu ký tự là chữ cái (A-Z)
        gia_tri = bang_ma[ky_tu]
    else:               # Nếu ký tự là số (0-9)
        gia_tri = int(ky_tu)
    trong_so = gia_tri * (2 ** a)
    tong_trong_so += trong_so
so_kiem_tra = tong_trong_so % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0
print("-" * 30)
print(f"Tổng các trọng số: {tong_trong_so}")
print(f"Số kiểm tra của mã container {container} là {so_kiem_tra}.")
