#a
def tinh_P(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2*i + 1)
    return tich

n = int(input("Nhập n: "))
print("P(n) =", tinh_P(n))
#b
def tinh_S(n):
    tong = 0
    for i in range(1, n + 1):
        tong += ((-1)**(i+1)) * i
    return tong

n = int(input("Nhập n: "))
print("S(n) =", tinh_S(n))
#c
def tinh_S(n):
    tong = 0
    for i in range(1, n + 1):
        tong += sum(range(1, i + 1))
    return tong

n = int(input("Nhập n: "))
print("S(n) =", tinh_S(n))
#d
def tinh_luy_thua(x, y):
    ket_qua = 1
    for i in range(y):
        ket_qua *= x
    return ket_qua

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("P(x, y) =", tinh_luy_thua(x, y))