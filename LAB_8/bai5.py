def cubesum(n):
    total = 0

    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    return total

def isArmstrong(n):
    return cubesum(n) == n

print("Cac so Armstrong tu 1 den 1000:")

for i in range(1, 1001):
    if isArmstrong(i):
        print(i)