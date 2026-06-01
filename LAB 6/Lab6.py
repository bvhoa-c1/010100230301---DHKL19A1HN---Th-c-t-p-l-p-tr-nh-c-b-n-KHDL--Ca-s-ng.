#bài 6.1
n = int(input("Nhap n: "))

a = []

for i in range(n):
    a.append(n)

sum_chan = sum(x for x in a if x % 2 == 0)
sum_le = sum(x for x in a if x % 2 != 0)

print("Tong chan =", sum_chan)
print("Tong le =", sum_le)
#bài 6.2
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):

        if n % i == 0:
            return False

    return True


def is_perfect(n):

    tong = 0

    for i in range(1, n):

        if n % i == 0:
            tong += i

    return tong == n


n = int(input("Nhap n: "))

a = []

for i in range(n):
    if n == {is_perfect}:
        print(f"{n} là số hoàn hảo")
        break
    else:
        print(f"{n} là số nguyên tố")
        break

#bài 6.3
a = list(map(float, input("Nhap day so: ").split()))

max_value = a[0]
min_value = a[0]


for x in a:

    if x > max_value:

        max_value = x


    if x < min_value:

        min_value = x


print("Gia tri lon nhat =", max_value)
print("Gia tri nho nhat =", min_value)
#bài 6.4
n = int(input("Nhap n: "))

fib = [0,1]

for i in range(n-2):

    fib.append(
        fib[-1] + fib[-2]
    )

print(fib[:n])

#bài 6.5
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):

        if n % i == 0:
            return False

    return True


primes = []

for i in range(100):

    if is_prime(i):

        primes.append(i)


print(primes)
#bài 6.6
a = list(map(int, input("Nhap day so: ").split()))


if len(a) < 2:

    print("Day phai co it nhat 2 phan tu")

else:

    d = a[1] - a[0]

    check = True


    for i in range(1, len(a)-1):

        if a[i+1] - a[i] != d:

            check = False
            break


    if check:

        print("La cap so cong")

    else:

        print("Khong phai")

#bài 6.7
m = int(input("Nhap so hang m: "))
n = int(input("Nhap so cot n: "))

matrix = []

print("Nhap ma tran:")

for i in range(m):

    row = list(
        map(int, input().split())
    )


    if len(row) != n:

        print("Nhap sai so cot")
        exit()


    matrix.append(row)


tong = 0


for i in range(m):

    for j in range(n):

        tong += matrix[i][j]


print("Tong =", tong)
#bài 6.8
m = int(input("So hang A: "))
n = int(input("So cot A: "))

A = []

for i in range(m):

    row = list(
        map(int, input().split())
    )

    A.append(row)


p = int(input("So cot B: "))

B = []

for i in range(n):

    row = list(
        map(int, input().split())
    )

    B.append(row)


C = []

for i in range(m):

    row = []

    for j in range(p):

        s = 0

        for k in range(n):

            s += A[i][k] * B[k][j]

        row.append(s)

    C.append(row)


for row in C:

    print(row)
#bài 6.9
n = int(input("Nhap cap ma tran: "))

A = []

print("Nhap ma tran:")

for i in range(n):

    row = list(
        map(int, input().split())
    )


    if len(row) != n:

        print("Nhap sai so cot")
        exit()


    A.append(row)


AT = []


for i in range(n):

    row = []


    for j in range(n):

        row.append(
            A[j][i]
        )


    AT.append(row)


print("Ma tran chuyen vi:")

for row in AT:

    print(row)


check = True


for i in range(n):

    for j in range(n):

        if A[i][j] != AT[i][j]:

            check = False
            break


if check:

    print("Ma tran doi xung")

else:

    print("Khong doi xung")

#bài 6.10
n = int(input("Nhap cap ma tran: "))

A = []

print("Nhap ma tran:")

for i in range(n):

    row = list(
        map(float, input().split())
    )

    A.append(row)


for i in range(n):

    for j in range(n):

        if i == j:

            A[i].append(1.0)

        else:

            A[i].append(0.0)


for i in range(n):

    pivot = A[i][i]

    if pivot == 0:

        print("Khong kha nghich")
        exit()


    for j in range(2*n):

        A[i][j] /= pivot


    for k in range(n):

        if k != i:

            factor = A[k][i]

            for j in range(2*n):

                A[k][j] -= factor * A[i][j]


print("Ma tran nghich dao:")

for i in range(n):

    print(A[i][n:])
