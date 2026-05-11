def factorial(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt


def permutation(n, r):
    return factorial(n) // factorial(n - r)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


n = int(input("Nhap n: "))
r = int(input("Nhap r: "))

print("Hoan vi P(n,r) =", permutation(n, r))
print("To hop C(n,r) =", combination(n, r))