

def tinh_S_b(n):
    s = 0
    for i in range(1, n + 1):
        s += ((-1) ** (i + 1)) * i
    return s

n = int(input("Nhập n: "))
print("S(n) =", tinh_S_b(n))