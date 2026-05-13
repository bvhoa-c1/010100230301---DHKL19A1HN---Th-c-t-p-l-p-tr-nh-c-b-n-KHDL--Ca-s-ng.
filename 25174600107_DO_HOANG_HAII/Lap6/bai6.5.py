def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 100) if is_prime(x)]

print(f"Các số nguyên tố nhỏ hơn 100: {primes}")
print(f"Tổng số: {len(primes)}")
