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

twin_primes = []

for num in range(2, 1000):
    if is_prime(num) and is_prime(num + 2):
        twin_primes.append((num, num + 2))

print("Các cặp số nguyên tố sinh đôi nhỏ hơn 1000:")
for pair in twin_primes:
    print(f"{pair[0]} và {pair[1]}")

print(f"\nTổng cộng: {len(twin_primes)} cặp")
