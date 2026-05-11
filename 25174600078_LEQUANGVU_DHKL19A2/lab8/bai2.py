def factorial(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt


n = int(input("Nhap n: "))
print(f"{n}! =", factorial(n))