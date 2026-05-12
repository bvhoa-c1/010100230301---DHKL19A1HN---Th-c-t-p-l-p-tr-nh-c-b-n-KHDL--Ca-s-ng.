#LAB_6
#Bài 6.1
n = int(input("Nhap n: "))
a = []

for i in range(n):
    x = int(input("Nhap phan tu: "))
    a.append(x)

tong_chan = 0
tong_le = 0

for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tong so chan:", tong_chan)
print("Tong so le:", tong_le)


#Bài 6.2
n = int(input("Nhap n: "))
a = []

for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

ket_qua = []

for x in a:
    nt = True
    if x < 2:
        nt = False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                nt = False
                break

    tong_uoc = 0
    for i in range(1, x):
        if x % i == 0:
            tong_uoc += i

    if nt or tong_uoc == x:
        ket_qua.append(x)

print("Cac so nguyen to hoac hoan hao:", ket_qua)


#Bài 6.3
a = list(map(float, input("Nhap day so: ").split()))

print("Gia tri lon nhat:", max(a))
print("Gia tri nho nhat:", min(a))


#Bài 6.4
n = int(input("Nhap n: "))

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

print("Day Fibonacci:", fib[:n])


#Bài 6.5
nguyen_to = []

for x in range(2, 100):
    ok = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ok = False
            break
    if ok:
        nguyen_to.append(x)

print("So nguyen to nho hon 100:", nguyen_to)


#Bài 6.6
a = list(map(int, input("Nhap day so: ").split()))

if len(a) < 3:
    print("La cap so cong")
else:
    d = a[1] - a[0]
    ok = True

    for i in range(1, len(a) - 1):
        if a[i + 1] - a[i] != d:
            ok = False
            break

    if ok:
        print("La cap so cong")
    else:
        print("Khong phai cap so cong")


#Bài 6.7
m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

A = []
for i in range(m):
    hang = list(map(float, input("Nhap hang: ").split()))
    A.append(hang)

tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]

print("Tong ma tran:", tong)


#Bài 6.8
m = int(input("Nhap so hang A: "))
n = int(input("Nhap so cot A: "))

A = []
for i in range(m):
    A.append(list(map(float, input("Nhap hang A: ").split())))

p = int(input("Nhap so hang B: "))
q = int(input("Nhap so cot B: "))

B = []
for i in range(p):
    B.append(list(map(float, input("Nhap hang B: ").split())))

if n != p:
    print("Khong the nhan hai ma tran")
else:
    C = []
    for i in range(m):
        hang = []
        for j in range(q):
            tong = 0
            for k in range(n):
                tong += A[i][k] * B[k][j]
            hang.append(tong)
        C.append(hang)

    print("Tich hai ma tran:")
    for hang in C:
        print(hang)


#Bài 6.9
n = int(input("Nhap cap ma tran vuong: "))

A = []
for i in range(n):
    A.append(list(map(float, input("Nhap hang: ").split())))

T = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[j][i])
    T.append(hang)

print("Ma tran chuyen vi:")
for hang in T:
    print(hang)

if A == T:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")


#Bài 6.10
n = int(input("Nhap cap ma tran vuong: "))

A = []
for i in range(n):
    A.append(list(map(float, input("Nhap hang: ").split())))

I = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1.0)
        else:
            hang.append(0.0)
    I.append(hang)

kha_nghich = True

for i in range(n):
    if A[i][i] == 0:
        for r in range(i + 1, n):
            if A[r][i] != 0:
                A[i], A[r] = A[r], A[i]
                I[i], I[r] = I[r], I[i]
                break

    if A[i][i] == 0:
        kha_nghich = False
        break

    pivot = A[i][i]

    for j in range(n):
        A[i][j] /= pivot
        I[i][j] /= pivot

    for r in range(n):
        if r != i:
            he_so = A[r][i]
            for j in range(n):
                A[r][j] -= he_so * A[i][j]
                I[r][j] -= he_so * I[i][j]

if not kha_nghich:
    print("Ma tran khong kha nghich")
else:
    print("Ma tran nghich dao:")
    for hang in I:
        print(hang)
