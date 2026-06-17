#Bài6.1:
n = int(input("Nhập số lượng phần tử: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

chan = [x for x in a if x % 2 == 0]
le = [x for x in a if x % 2 != 0]

print(f"Tổng các số chẵn ({chan}): {sum(chan)}")
print(f"Tổng các số lẻ ({le}): {sum(le)}")

#Bài6.2:
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong == n

a = [6, 7, 13, 28, 10, 11] 
ket_qua = [x for x in a if la_so_nguyen_to(x) or la_so_hoan_hao(x)]
print(f"Các số thỏa mãn: {ket_qua}")

#Bài6.3:
a = [1.5, 10, -3.2, 50, 25.4]
print(f"Giá trị lớn nhất: {max(a)}")
print(f"Giá trị nhỏ nhất: {min(a)}")

#Bài6.4:
n = int(input("Nhập n: "))
fibo = [0, 1]
for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])
print(f"Dãy Fibonacci: {fibo[:n]}")

# Bài 6.5:
import math

n_to = [x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))]

print(n_to)

#Bài6.6:
a = [2, 4, 6, 8, 10] 
csc = True
if len(a) < 2:
    is_csc = True
else:
    d = a[1] - a[0]
    for i in range(1, len(a) - 1):
        if a[i+1] - a[i] != d:
            csc = False
            break

print("Dãy là cấp số cộng" if csc else "Không phải cấp số cộng")

#Bài6.7:
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

tong = 0

for row in matrix:
    tong += sum(row)

print("Tổng ma trận =", tong)

#Bài6.8:
m = int(input("Nhập số hàng ma trận A: "))
n = int(input("Nhập số cột ma trận A: "))
A = []

print("Nhập ma trận A:")
for i in range(m):
    A.append(list(map(int, input().split())))

p = int(input("Nhập số cột ma trận B: "))
B = []

print("Nhập ma trận B:")
for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0 for j in range(p)] for i in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
print("Tích hai ma trận:")
for row in C:
    print(row)

#Bài6.9:
n = int(input("Nhập cặp ma trận vuông: "))

A = []

for i in range(n):
    A.append(list(map(int, input().split())))

AT = []

for j in range(n):
    row = []
    for i in range(n):
        row.append(A[i][j])
    AT.append(row)

print("Ma trận chuyển vị:")

for row in AT:
    print(row)
if A == AT:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")

#Bài6.10:
print("Nhập ma trận 2x2")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

det = a * d - b * c

if det == 0:
    print("Ma trận không khả nghịch")
else:
    print("Ma trận nghịch đảo:")

    print(f"{d/det}   {-b/det}")
    print(f"{-c/det}   {a/det}")