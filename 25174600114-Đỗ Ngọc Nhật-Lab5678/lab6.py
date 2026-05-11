#6.1
n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    x = int(input())
    a.append(x)

tong_chan = 0
tong_le = 0

for i in a:
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)


#6.2
def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    a.append(int(input()))

print("Các số nguyên tố hoặc hoàn hảo:")

for i in a:
    if nguyen_to(i) or hoan_hao(i):
        print(i, end=" ")



#6.3
n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    a.append(float(input()))

print("Max =", max(a))
print("Min =", min(a))


#6.4
n = int(input("Nhập n: "))

fibo = [0, 1]

[fibo.append(fibo[-1] + fibo[-2]) for i in range(2, n)]

print(fibo[:n])



#6.5
prime = [x for x in range(2, 100)
         if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

print(prime)


#6.6
n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    a.append(int(input()))

d = a[1] - a[0]
kt = True

for i in range(1, n - 1):
    if a[i + 1] - a[i] != d:
        kt = False
        break

if kt:
    print("Là cấp số cộng")
else:
    print("Không phải cấp số cộng")



#6.7
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

a = []
tong = 0

for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

for i in a:
    tong += sum(i)

print("Tổng ma trận =", tong)


#6.8
m = int(input("Số hàng A: "))
n = int(input("Số cột A = số hàng B: "))
p = int(input("Số cột B: "))

A = []
B = []

print("Nhập ma trận A:")
for i in range(m):
    A.append(list(map(int, input().split())))

print("Nhập ma trận B:")
for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0 for j in range(p)] for i in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Ma trận tích:")

for i in C:
    print(i)



#6.9
n = int(input("Nhập cấp ma trận: "))

A = []

for i in range(n):
    A.append(list(map(int, input().split())))

AT = [[A[j][i] for j in range(n)] for i in range(n)]

print("Ma trận chuyển vị:")
for i in AT:
    print(i)

if A == AT:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")



#6.10
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

det = a*d - b*c

if det == 0:
    print("Ma trận không khả nghịch")
else:
    print("Ma trận nghịch đảo:")

    print([d/det, -b/det])
    print([-c/det, a/det])