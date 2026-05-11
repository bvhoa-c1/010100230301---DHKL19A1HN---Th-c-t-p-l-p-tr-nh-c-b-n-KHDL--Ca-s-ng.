def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(n, r):
    return factorial(n) // (
        factorial(r) * factorial(n - r)
    )

n = int(input("Nhap n: "))
r = int(input("Nhap r: "))

print("Hoan vi =", permutation(n, r))
print("To hop =", combination(n, r))