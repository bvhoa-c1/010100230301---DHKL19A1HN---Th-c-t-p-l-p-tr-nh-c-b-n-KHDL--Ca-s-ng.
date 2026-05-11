def cubesum(n):
    return sum(int(ch) ** 3 for ch in str(abs(n)))

def isArmstrong(n):
    return n >= 0 and cubesum(n) == n

limit = int(input("limit = "))
print([n for n in range(limit + 1) if isArmstrong(n)])
