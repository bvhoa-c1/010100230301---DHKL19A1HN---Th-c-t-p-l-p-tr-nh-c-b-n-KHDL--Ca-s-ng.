# bài 6.1
n = int(input("Nhập số phần tử: "))

arr = []

for i in range(n):
    x = int(input("Nhập phần tử: "))
    arr.append(x)

chan = 0
le = 0

for x in arr:
    if x % 2 == 0:
        chan += x
    else:
        le += x

print("Tổng chẵn:", chan)
print("Tổng lẻ:", le)
# bài 6.2
def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def la_hoan_hao(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong == n

n = int(input("Nhập số phần tử: "))
arr = []

for i in range(n):
    arr.append(int(input("Nhập phần tử: ")))

for x in arr:
    if la_nguyen_to(x) or la_hoan_hao(x):
        print(x)
    # bài 6.3
    n = int(input("Nhập số phần tử: "))

arr = []

for i in range(n):
    arr.append(float(input("Nhập phần tử: ")))

print("Giá trị lớn nhất:", max(arr))
print("Giá trị nhỏ nhất:", min(arr))
# bài 6.4
n = int(input("Nhập n: "))

fib = [0, 1]

[fib.append(fib[-1] + fib[-2]) for i in range(n - 2)]

print(fib[:n])
# bài 6.5
def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

primes = [x for x in range(100) if la_nguyen_to(x)]

print(primes)
# bài 6.6
arr = list(map(int, input("Nhập dãy số: ").split()))

if len(arr) < 2:
    print("Không đủ phần tử")
else:
    d = arr[1] - arr[0]

    la_cap_so_cong = True
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            la_cap_so_cong = False
            break

    if la_cap_so_cong:
        print("Là cấp số cộng")
    else:
        print("Không phải cấp số cộng")
        # bài 6.7
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

s = 0

for row in matrix:
    s += sum(row)

print("Tổng ma trận:", s)
# bài 6.8
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print("Ma trận tích:")

for row in result:
    print(row)
# bài 6.9
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

transpose = []

for i in range(len(matrix[0])):
    row = []

    for j in range(len(matrix)):
        row.append(matrix[j][i])

    transpose.append(row)

print("Ma trận chuyển vị:")

for row in transpose:
    print(row)

if matrix == transpose:
    print("Ma trận đối xứng")
else:
    print("Không đối xứng")
# bài 6.10
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