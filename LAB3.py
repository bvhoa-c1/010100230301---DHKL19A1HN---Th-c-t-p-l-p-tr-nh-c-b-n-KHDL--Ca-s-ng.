#MSV:25174600049
#HỌ VÀ TÊN:NGUYỄN THỊ THANH HUYỀN

#BÀI 1:
#a)
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng là:", tong)
#b)
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng là:", tong)

#BÀI2:
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:4}", end="")
    print()

#BÀI3:

n = int(input("Nhập số hàng"))
for i in range (1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print("", end="")
    print()

#BÀI4:
n = 0
while n <= 0:
    n = int(input("Nhập lại n > 0: "))
s1 = 0
for i in range(1, n + 1):
    s1 += i
s2 = 0
for i in range(1, n + 1):
    s2 += 1 / i
import math
s3 = 0
for i in range(1, n + 1):
    s3 += 1 / math.sqrt(2 * i)
s4 = 0
for i in range(1, n + 1):
    s4 += ((-1) ** (i + 1)) / i

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)

#BÀI5:
for i in range(1, 1001):
    if int(i ** 0.5) ** 2 == i:
        print(i, end="")

#BÀI6:
n = int(input("Nhập n:"))
S = 0
for i in range(1, n + 1):
    S += 1 / i
print("Tổng =", S)

#BÀI7:
n = int(input("Nhập n:"))
count = 0
for i in range(1, n + 1):
    s = sum(int(d) for d in str(i))
    if s % 2 == 0:
        count += 1
print("Số lượng =", count)
#BÀI8:
n = int(input("Nhập n: "))
max_sum = 0
number = 0
for i in range(1, n + 1):
    s = sum(int(d) for d in str(i))
    if s > max_sum:
        max_sum = s
        number = i
print("Số cần tìm:", number)

#BÀI9:
n = int(input("Nhập n: "))
max_uoc = 0
so = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count > max_uoc:
        max_uoc = count
        so = i

print("Số có nhiều ước nhất:", so)
#BÀI11:
n = int(input("Nhập n: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#BÀI12:
s = input("Nhập mã container (10 ký tự): ")

# Bảng mã
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38]

mapping = {}
for i in range(len(letters)):
    mapping[letters[i]] = values[i]

total = 0

for i in range(len(s)):
    c = s[i]
    if c.isalpha():
        v = mapping[c]
    else:
        v = int(c)
    total += v * (2 ** i)

check = total % 11
if check == 10:
    check = 0

print("Check digit =", check)







