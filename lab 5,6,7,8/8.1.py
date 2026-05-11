# Kiểm tra số nguyên tố và tìm các cặp số nguyên tố sinh đôi < 1000

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


for i in range(2, 1000):
    if isPrime(i) and isPrime(i + 2):
        print((i, i + 2))