def is_prime(x):
    if x < 2: return False
    for i in range(2, x):
        if x % i == 0: return False
    return True
primes = [x for x in range(2, 100) if is_prime(x)]
print(primes)