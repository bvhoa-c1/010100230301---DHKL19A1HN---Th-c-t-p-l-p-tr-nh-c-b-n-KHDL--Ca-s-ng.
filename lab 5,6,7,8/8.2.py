# Hàm tính giai thừa

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


n = int(input("Nhập n: "))

print("Giai thừa =", factorial(n))