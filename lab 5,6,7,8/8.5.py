# Kiểm tra số Armstrong

def cubesum(n):
    total = 0

    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    return total


def isArmstrong(n):
    return n == cubesum(n)


print("Các số Armstrong từ 1 đến 1000:")

for i in range(1, 1001):
    if isArmstrong(i):
        print(i)