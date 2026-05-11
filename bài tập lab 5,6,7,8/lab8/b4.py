def cubesum(n):
    s = 0
    for ch in str(n):
        d = int(ch)
        s += d * d * d
    return s
print(cubesum(123))