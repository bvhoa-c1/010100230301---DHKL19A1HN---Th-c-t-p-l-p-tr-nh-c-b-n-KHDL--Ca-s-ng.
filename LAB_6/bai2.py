def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def BCNN(a, b):
    return abs(a * b) // UCLN(a, b)

def rut_gon(tu, mau):
    ucln = UCLN(tu, mau)
    return tu // ucln, mau // ucln

def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

# Nhập dữ liệu
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print("UCLN:", UCLN(a, b))
print("BCNN:", BCNN(a, b))

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu_rg, mau_rg = rut_gon(tu, mau)
print("Phân số rút gọn:", tu_rg, "/", mau_rg)

x = int(input("Nhập số 1: "))
y = int(input("Nhập số 2: "))
z = int(input("Nhập số 3: "))
mn, mx = min_max(x, y, z)
print("Nhỏ nhất:", mn)
print("Lớn nhất:", mx)