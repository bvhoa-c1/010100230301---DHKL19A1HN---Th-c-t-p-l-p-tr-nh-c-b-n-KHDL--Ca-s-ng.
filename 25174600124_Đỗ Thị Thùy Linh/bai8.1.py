import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

print("Cac cap so nguyen to sinh doi < 1000:")

for i in range(2, 1000):
    if isPrime(i) and isPrime(i + 2):
        print((i, i + 2))