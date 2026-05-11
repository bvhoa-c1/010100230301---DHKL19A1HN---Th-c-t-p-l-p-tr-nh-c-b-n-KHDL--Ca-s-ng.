def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = int(input("Nhap so phan tu: "))

a = []
for i in range(n):
    a.append(int(input()))

print("So nguyen to:")
for x in a:
    if is_prime(x):
        print(x, end=" ")

print("\nSo hoan hao:")
for x in a:
    if is_perfect(x):
        print(x, end=" ")