def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutation(n, r):
    if r < 0 or r > n:
        return None
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if r < 0 or r > n:
        return None
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("n = "))
r = int(input("r = "))

print(permutation(n, r))
print(combination(n, r))
