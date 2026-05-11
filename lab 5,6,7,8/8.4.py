# Hàm cubesum

def cubesum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10

    return total


n = int(input("Nhập số: "))

print("Tổng lập phương các chữ số =", cubesum(n))