# Bài 8.1: Hàm kiểm tra số nguyên tố và tìm cặp số nguyên tố sinh đôi

def is_prime(n):
    """Kiểm tra xem n có phải số nguyên tố"""
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

# Tìm tất cả cặp số nguyên tố sinh đôi < 1000
twin_primes = []

for n in range(2, 1000):
    if is_prime(n) and is_prime(n + 2):
        twin_primes.append((n, n + 2))

print("Cặp số nguyên tố sinh đôi nhỏ hơn 1000:")
print("-" * 40)
for pair in twin_primes:
    print(f"{pair[0]} và {pair[1]}")

print(f"\nTổng cộng: {len(twin_primes)} cặp số nguyên tố sinh đôi")
