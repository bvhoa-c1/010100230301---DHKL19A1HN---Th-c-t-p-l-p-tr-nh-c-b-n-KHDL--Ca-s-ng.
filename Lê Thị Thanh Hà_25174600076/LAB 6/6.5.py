def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


primes = [x for x in range(100) if is_prime(x)]

print("Các số nguyên tố nhỏ hơn 100:")
print(primes)