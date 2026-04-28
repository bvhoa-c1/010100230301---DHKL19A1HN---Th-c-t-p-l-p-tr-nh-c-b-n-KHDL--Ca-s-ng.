#a
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN:", ucln(a, b))
#b
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

print("BCNN:", bcnn(a, b))
#c
def rut_gon(tu, mau):
    u = ucln(tu, mau)
    return tu // u, mau // u

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

tu_rg, mau_rg = rut_gon(tu, mau)
print("Phân số rút gọn:", tu_rg, "/", mau_rg)
#d
def tim_min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

mn, mx = tim_min_max(x, y, z)
print("Số nhỏ nhất:", mn)
print("Số lớn nhất:", mx)