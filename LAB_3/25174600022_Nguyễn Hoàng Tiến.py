import math
#bài 1
#a

tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("tổng các số chia hết cho 7 nhưng không chi hết cho 5: ", tong)
#b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("tổng các số chia hết cho 4 nhưng không chia hết cho 6: ", tong)

#bài 2
print("-------------------BẢNG CỬU CHƯƠNG-------------------")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}x{i}={i*j}", end = "\t")
    print()
print("-----------------------------------------------------")

#bài 3
n = int(input("nhập số hàng tam giác vuông rỗng: "))
for i in range(1, n+1):
    if i == n:
        print("x"*i)
    else:
        for j in range(1, i+1):
            if j == 1 or j == i:
                print("x", end = "")
            else:
                print(" ", end = "")
        print()
#bài 4
n = int(input("nhập n là số nguyên dương: "))
if n <= 0:
    print("vui lòng nhập lại theo đúng yêu cầu! nếu tiếp tục sai sẽ dừng chương trình!")
    n = int(input("nhập n là số nguyên dương: "))
S1 = 0
S2 = 0
S3 = 0
S4 = 0
#a
for i in range(1, n+1):
    S1 += i
print("S1 =", S1)
#b
for i in range(1, n+1):
    S2 += 1/i
print("S2 =", S2)
#c
for i in range(1, n+1):
    S3 += 1/(math.sqrt(2*i))
print("S3 =", S3)
#d
for i in range(1, n+1):
    S4 += (-1)**(i+1)/i
print("S4 =", S4)

#bài 5
print("số chính phương trong khoảng từ 1 đến 1000:")
for i in range(1,1001):
    if math.sqrt(i).is_integer():
        print(i, end =", ")
print()

#bài 6
n = int(input("nhập n để tính tổng nghịch đảo:"))
S1 = 0
for i in range(1, n+1):
    S1 += 1/i
print("tổng nghịch đảo của S1: ", S1)

#bài 7
n = int(input("nhập n: "))
so_luong = 0
for i in range(1, n+1):
    s = str(i)
    tong = sum(int(j) for j in s)
    if tong % 2 == 0:
        so_luong += 1
print("số lượng số có tổng chữ số là số chẵn là: ", so_luong)

#bài 8
n = int(input("nhập n: "))
lon_nhat = 0
tong_lon_nhat = 0
for i in range(1, n+1):
    s = str(i)
    tong = sum(int(j) for j in s)
    if tong > tong_lon_nhat:
        tong_lon_nhat = tong
        lon_nhat = i
print(f"số có tổng chữ số lớn nhất trong khoảng từ 1 đến {n} là: ", lon_nhat)

#bài 9
n = int(input("nhập n: "))
max_uoc = 0
so_max = 0
for i in range(1, n+1):
    dem = 0
    for j in range(1, i+1):
        if i % j == 0:
            dem += 1
    if dem > max_uoc:
        max_uoc = dem
        so_max = i
print(f"số có nhiều ước nhất trong khoảng từ 1 đến {n} là: ", so_max)

#bài 11
n = int(input("nhập n:"))
F1 = 0
F2 = 1
print(f"dãy {n} số Fibonacci: ")
for i in range(n):
    print(F1, end =" ")
    F1, F2 = F2, F1 + F2
print()

#bài 12
bang = {
"A":10,"B":12,"C":13,"D":14,"E":15,"F":16,"G":17,"H":18,"I":19,"J":20,
"K":21,"L":23,"M":24,"N":25,"O":26,"P":27,"Q":28,"R":29,"S":30,"T":31,
"U":32,"V":34,"W":35,"X":36,"Y":37,"Z":38
}
s = input("nhập mã container: ")
tong = 0
for i in range(len(s)):
    if s[i].isalpha():
        gia_tri = bang[s[i]]
    else:
        gia_tri = int(s[i])
    w = gia_tri * (2**i)
    tong += w
check_digit = tong % 11
if check_digit == 10:
    check_digit = 0
print(f"số kiểm tra của mã container {s} là {check_digit}")
