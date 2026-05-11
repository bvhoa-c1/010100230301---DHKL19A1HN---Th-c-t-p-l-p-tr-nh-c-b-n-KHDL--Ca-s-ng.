# Tính tổng các ước số thực sự

def sumDivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total


n = int(input("Nhập số: "))

print("Tổng ước số =", sumDivisors(n))