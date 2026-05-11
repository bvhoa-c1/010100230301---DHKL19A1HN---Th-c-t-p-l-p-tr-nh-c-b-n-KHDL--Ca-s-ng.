import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def isPerfect(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong == n

n = int(input("Nhap n: "))

a = []

for i in range(n):
    a.append(int(input()))

print("Cac so nguyen to hoac hoan hao:")

for x in a:
    if isPrime(x) or isPerfect(x):
        print(x, end=" ")