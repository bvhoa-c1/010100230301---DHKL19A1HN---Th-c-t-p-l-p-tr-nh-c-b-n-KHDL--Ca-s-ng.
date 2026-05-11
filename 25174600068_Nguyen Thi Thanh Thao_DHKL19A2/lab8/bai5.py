def cubesum(n):
    tong = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        tong += digit ** 3
        temp //= 10

    return tong


def isArmstrong(n):
    return n == cubesum(n)


print("Cac so Armstrong < 1000:")

for i in range(1, 1000):
    if isArmstrong(i):
        print(i)