# bài 1
# a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i

print("Tổng =", tong)
# b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i

print("Tổng =", tong)
# bài 2
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()

# bài 3
n = int(input("Nhập số hàng: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# bài 5
for i in range(1, 1001):
    if int(i**0.5) ** 2 == i:
        print(i)

# bài 6
n = int(input("Nhập n: "))
S = 0

for i in range(1, n + 1):
    S += 1/i

print("Tổng =", S)

# bài 7
n = int(input("Nhập n: "))
dem = 0

for i in range(1, n + 1):
    tong = 0
    for digit in str(i):
        tong += int(digit)

    if tong % 2 == 0:
        dem += 1

print("Số lượng =", dem)
# bài 8
n = int(input("Nhập n: "))

max_sum = 0
so_max = 0

for i in range(1, n + 1):
    tong = sum(int(d) for d in str(i))

    if tong > max_sum:
        max_sum = tong
        so_max = i

print("Số =", so_max)
print("Tổng chữ số =", max_sum)
# bài 9
n = int(input("Nhập n: "))

max_uoc = 0
so_max = 0

for i in range(1, n + 1):
    dem = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem += 1

    if dem > max_uoc:
        max_uoc = dem
        so_max = i

print("Số có nhiều ước nhất:", so_max)
print("Số lượng ước:", max_uoc)

# bài 11
n = int(input("Nhập n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# bài 12
container = input("Nhập mã container: ")

bang = {
"A":10,"B":12,"C":13,"D":14,"E":15,"F":16,"G":17,"H":18,"I":19,"J":20,
"K":21,"L":23,"M":24,"N":25,"O":26,"P":27,"Q":28,"R":29,"S":30,"T":31,
"U":32,"V":34,"W":35,"X":36,"Y":37,"Z":38
}

tong = 0

for i in range(len(container)):
    k = container[i]

    if k.isalpha():
        value = bang[k]
    else:
        value = int(k)

    tong += value * (2 ** i)

check = tong % 11

if check == 10:
    check = 0

print("Số kiểm tra:", check)    