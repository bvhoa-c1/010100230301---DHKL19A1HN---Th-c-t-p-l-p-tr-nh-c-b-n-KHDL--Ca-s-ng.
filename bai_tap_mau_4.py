# a: Tính P(n) = 1 * 3 * 5 * ... * (2n+1)
def tinh_P_a(n):
    p = 1
    for i in range(n + 1):
        p *= (2 * i + 1)
    return p

n = int(input("Nhập n: "))
print("P(n) =", tinh_P_a(n))


# b: Tính S(n) = 1 - 2 + 3 - 4 + ... + ((-1)^(n+1))*n
def tinh_S_b(n):
    s = 0
    for i in range(1, n + 1):
        s += ((-1) ** (i + 1)) * i
    return s

n = int(input("Nhập n: "))
print("S(n) =", tinh_S_b(n))


# c: Tính S(n) = 1 + (1+2) + (1+2+3) + ... + (1+2+3+...+n)
def tinh_S_c(n):
    s = 0
    tong_phu = 0
    for i in range(1, n + 1):
        tong_phu += i
        s += tong_phu
    return s

n = int(input("Nhập n: "))
print("S(n) =", tinh_S_c(n))


# d: Tính P(x, y) = x^y
def tinh_P_d(x, y):
    return x ** y

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("P(x, y) =", tinh_P_d(x, y))