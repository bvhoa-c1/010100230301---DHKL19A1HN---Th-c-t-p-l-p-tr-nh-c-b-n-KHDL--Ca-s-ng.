# Bài 6.1
# Nhập mảng và tính tổng chẵn, lẻ

n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

tong_chan = 0
tong_le = 0

for i in a:
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print("Danh sách:", a)
print("Tổng số chẵn =", tong_chan)
print("Tổng số lẻ =", tong_le)
# Bài 6.2
# In các số nguyên tố hoặc số hoàn hảo

import math

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

print("Các số nguyên tố hoặc hoàn hảo:")

for i in a:
    if so_nguyen_to(i) or so_hoan_hao(i):
        print(i, end=" ")

# Bài 6.3
# Tìm số lớn nhất và nhỏ nhất

n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

print("Danh sách:", a)
print("Giá trị lớn nhất:", max(a))
print("Giá trị nhỏ nhất:", min(a))

# Bài 6.4
# List Comprehension Fibonacci

n = int(input("Nhập n: "))

fibo = [0, 1]

[fibo.append(fibo[-1] + fibo[-2]) for i in range(2, n)]

print("Dãy Fibonacci:")
print(fibo[:n])

# Bài 6.5
# Danh sách số nguyên tố nhỏ hơn 100

import math

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_list = [i for i in range(100) if so_nguyen_to(i)]

print("Các số nguyên tố < 100:")
print(prime_list)

# Bài 6.6
# Kiểm tra cấp số cộng

n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

if n < 2:
    print("Không đủ phần tử")
else:
    d = a[1] - a[0]
    check = True

    for i in range(1, n - 1):
        if a[i + 1] - a[i] != d:
            check = False
            break

    if check:
        print("Dãy là cấp số cộng")
    else:
        print("Dãy không phải cấp số cộng")

# Bài 6.7
# Tính tổng ma trận

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        row.append(x)
    matrix.append(row)

tong = 0

for row in matrix:
    tong += sum(row)

print("Ma trận:")
for row in matrix:
    print(row)

print("Tổng các phần tử =", tong)

# Bài 6.8
# Nhân hai ma trận

m = int(input("Nhập số hàng ma trận A: "))
n = int(input("Nhập số cột ma trận A: "))

A = []

for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        row.append(x)
    A.append(row)

p = int(input("Nhập số hàng ma trận B: "))
q = int(input("Nhập số cột ma trận B: "))

B = []

for i in range(p):
    row = []
    for j in range(q):
        x = int(input(f"B[{i}][{j}] = "))
        row.append(x)
    B.append(row)

if n != p:
    print("Không thể nhân hai ma trận")
else:
    C = [[0 for j in range(q)] for i in range(m)]

    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    print("Ma trận tích:")

    for row in C:
        print(row)

# Bài 6.9
# Ma trận chuyển vị và kiểm tra đối xứng

n = int(input("Nhập cấp ma trận vuông: "))

A = []

for i in range(n):
    row = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        row.append(x)
    A.append(row)

transpose = [[A[j][i] for j in range(n)] for i in range(n)]

print("Ma trận chuyển vị:")

for row in transpose:
    print(row)

if A == transpose:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")     

# Bài 6.10
# Bài 6.10 đơn giản - ma trận nghịch đảo 2x2

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

    print([d/det, -b/det])
    print([-c/det, a/det])

    

