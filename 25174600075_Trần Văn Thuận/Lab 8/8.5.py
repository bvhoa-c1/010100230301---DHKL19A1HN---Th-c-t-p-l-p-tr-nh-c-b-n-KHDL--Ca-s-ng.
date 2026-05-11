def cubesum(n):
    tong = 0
    temp = n
    while temp > 0:
        so = temp % 10
        tong += so**3
        temp //= 10
    return tong
def armstrong(n):
    return cubesum(n) == n
print("Các số armstrong nhỏ hơn 1000:")
for i in range(1, 1000):
    if armstrong(i):
        print(i, end=' ')