

def tinh_P_a(n):
    p = 1
    for i in range(n + 1):
        p *= (2 * i + 1)
    return p

n = int(input("Nhập n: "))
print("P(n) =", tinh_P_a(n))