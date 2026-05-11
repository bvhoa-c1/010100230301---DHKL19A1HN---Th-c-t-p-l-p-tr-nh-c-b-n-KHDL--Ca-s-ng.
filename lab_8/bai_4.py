def cubesum(n):
    return sum(int(ch) ** 3 for ch in str(abs(n)))

n = int(input("n = "))
print(cubesum(n))
