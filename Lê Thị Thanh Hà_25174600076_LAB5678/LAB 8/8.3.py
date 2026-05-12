def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def arrangement(n, r):
    return factorial(n) // factorial(n - r)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

print("Chỉnh hợp:", arrangement(n, r))
print("Tổ hợp:", combination(n, r))
