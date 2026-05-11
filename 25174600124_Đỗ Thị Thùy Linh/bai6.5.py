import math

prime = [
    x for x in range(2, 100)
    if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))
]

print(prime)