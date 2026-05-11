# Tính hoán vị và tổ hợp

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

print("Hoán vị =", permutation(n, r))
print("Tổ hợp =", combination(n, r))