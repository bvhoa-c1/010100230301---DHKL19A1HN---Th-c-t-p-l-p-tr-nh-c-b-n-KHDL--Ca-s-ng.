# Bài 6.5: Tạo danh sách số nguyên tố < 100 sử dụng List Comprehension

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sử dụng List Comprehension
primes = [n for n in range(100) if is_prime(n)]

print(f"Tất cả số nguyên tố nhỏ hơn 100:")
print(primes)
print(f"\nTổng số nguyên tố: {len(primes)}")
