#Bài 1
# a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng a =", tong)

# b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng b =", tong)
#Bài 2
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:4}", end="")
    print()
#Bài 3
n = int(input("Nhập số hàng: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#Bài 4
import math

# nhập n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n > 0: "))

S1 = 0
S2 = 0
S3 = 0
S4 = 0

for i in range(1, n + 1):
    S1 += i
    S2 += 1 / i
    S3 += 1 / math.sqrt(2 * i)
    S4 += ((-1) ** (i + 1)) / i

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
#Bài 5
for i in range(1, 1001):
    if int(i**0.5)**2 == i:
        print(i, end=" ")
#Bài 6
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += 1/i
print("S =", S)
#Bài 7
n = int(input("Nhập n: "))
dem = 0

for i in range(1, n+1):
    s = sum(map(int, str(i)))
    if s % 2 == 0:
        dem += 1

print("Số lượng =", dem)
#Bài 8
n = int(input("Nhập n: "))
max_sum = 0
so = 0

for i in range(1, n+1):
    s = sum(map(int, str(i)))
    if s > max_sum:
        max_sum = s
        so = i

print("Số =", so)
#Bài 9
n = int(input("Nhập n: "))
max_uoc = 0
so = 0

for i in range(1, n+1):
    dem = 0
    for j in range(1, i+1):
        if i % j == 0:
            dem += 1
    if dem > max_uoc:
        max_uoc = dem
        so = i

print("Số có nhiều ước nhất:", so)
#Bài 11
n = int(input("Nhập n: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#Bài 12
s = input("Nhập mã container: ")

bang = {
"A":10,"B":12,"C":13,"D":14,"E":15,"F":16,"G":17,"H":18,"I":19,"J":20,
"K":21,"L":23,"M":24,"N":25,"O":26,"P":27,"Q":28,"R":29,"S":30,"T":31,
"U":32,"V":34,"W":35,"X":36,"Y":37,"Z":38
}

tong = 0

for i in range(len(s)):
    if s[i].isalpha():
        val = bang[s[i]]
    else:
        val = int(s[i])
    tong += val * (2 ** i)

check = tong % 11
if check == 10:
    check = 0

print("Check digit =", check)