import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    total = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

n = int(input("n = "))
a = list(map(int, input("array = ").split()))[:n]

print([x for x in a if is_prime(x) or is_perfect(x)])
