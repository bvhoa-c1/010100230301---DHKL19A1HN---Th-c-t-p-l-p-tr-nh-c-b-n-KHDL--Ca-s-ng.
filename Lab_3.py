import math

# Bài 1: Tính tổng dãy số [cite: 5]
# a) Chia hết cho 7 nhưng không chia hết cho 5 trong [2000, 4000] [cite: 6, 7]
tong_a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong_a += i

# b) Chia hết cho 4 nhưng không chia hết cho 6 trong [500, 1000] [cite: 8, 9]
tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i

# Bài 2: In bảng cửu chương từ 1 đến 9 dạng bảng 2 chiều [cite: 10, 11]
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} x {i} = {i*j:<5}", end=" | ")
    print()

# Bài 3: Vẽ tam giác vuông rỗng [cite: 12, 13]
n = 5 
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")

# Bài 4: Tính các tổng S1, S2, S3, S4 [cite: 19, 21, 22, 23, 24, 25]
n = 0
while n <= 0: 
    n = 3 
s1 = s2 = s3 = s4 = 0
for i in range(1, n + 1):
    s1 += i
    s2 += 1 / i
    s3 += 1 / math.sqrt(2 * i)
    s4 += ((-1)**(i + 1)) / i

# Bài 5: In số chính phương từ 1 đến 1000 
print("Số chính phương:")
for i in range(1, 1001):
    c = int(math.sqrt(i))
    if c * c == i:
        print(i, end=" ")
print()

char_values = {
    'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19, 'J':20, 
    'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27, 'Q':28, 'R':29, 'S':30, 'T':31, 
    'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38
}
container = "SUDU307007" 
tong_trong_so = 0

for i in range(10): 
    ky_tu = container[i]
    gia_tri = char_values[ky_tu] if ky_tu.isalpha() else int(ky_tu) 
    tong_trong_so += gia_tri * (2 ** i) 

so_kiem_tra = tong_trong_so % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0
print(f"Số kiểm tra của {container} là: {so_kiem_tra}")
#bài 6: Viết chương trình tính tổng nghịch đảo của số nguyên đầu tiên
n = int(input("Nhập n: "))
s1 = 0
for i in range(1, n + 1):
    s1 += 1 / i
print(f"Tổng S1 = {s1}")
#Bài 7: Nhập n. Đếm số lượng số trong khoảng [1, n] có tổng chữ số là số chẵn.
n = int(input("Nhập n: "))
count = 0
for i in range(1, n + 1):
    # Ép kiểu số thành chuỗi để tách từng chữ số, rồi cộng lại
    tong_cs = sum(int(digit) for digit in str(i))
    if tong_cs % 2 == 0:
        count += 1
print(f"Số lượng số có tổng chữ số chẵn: {count}")

#Bài 8: Nhập n. Tìm số có tổng chữ số lớn nhất trong khoảng từ 1 đến n.
n = int(input("Nhập n: "))
max_tong = 0
so_max = 1
for i in range(1, n + 1):
    tong_cs = sum(int(digit) for digit in str(i))
    if tong_cs > max_tong:
        max_tong = tong_cs
        so_max = i
print(f"Số có tổng chữ số lớn nhất là {so_max} (tổng = {max_tong})")


#Bài 9: Nhập n. Tìm số có nhiều ước nhất trong khoảng từ 1 đến n.
n = int(input("Nhập n: "))
max_uoc = 0
so_nhieu_uoc = 1

for i in range(1, n + 1):
    dem_uoc = 0
    # Đếm số lượng ước của i
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    
    # Cập nhật nếu tìm thấy số có nhiều ước hơn
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_nhieu_uoc = i

print(f"Số có nhiều ước nhất là {so_nhieu_uoc} (có {max_uoc} ước)")

#Bài 11: In ra n số Fibonacci đầu tiên bằng vòng lặp for.
n = int(input("Nhập n: "))
f1, f2 = 1, 1

print(f"{n} số Fibonacci đầu tiên là:", end=" ")
for i in range(n):
    if i == 0:
        print(f1, end=" ")
    elif i == 1:
        print(f2, end=" ")
    else:
        fn = f1 + f2
        print(fn, end=" ")
        f1 = f2
        f2 = fn
print()