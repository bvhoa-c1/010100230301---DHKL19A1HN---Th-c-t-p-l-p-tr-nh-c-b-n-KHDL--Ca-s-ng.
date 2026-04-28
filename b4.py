def cau_a(n):
    p = 1
    for i in range(1, 2 * n + 2, 2):
        p *= i
    return p


def cau_b(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            s += i
        else:
            s -= i
    return s


def cau_c(n):
    s = 0
    tong = 0
    for i in range(1, n + 1):
        tong += i
        s += tong
    return s


def tinh_P_d(x, y):
    return x ** y


n = int(input("Nhập n: "))

print("Câu a:")
print("P(n) =", cau_a(n))

print("Câu b:")
print("S(n) =", cau_b(n))

print("Câu c:")
print("S(n) =", cau_c(n))

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

print("Câu d:")
print("P(x,y) =", tinh_P_d(x, y))