

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


n = int(input("Nhap so luong phan tu: "))

arr = [int(input()) for _ in range(n)]

result = []

for x in arr:
    if is_prime(x) or is_perfect(x):
        result.append(x)

print("Cac phan tu thoa man:", result)