import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
#a
ucln = math.gcd(a, b)
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
#b
bcnn = abs(a*b)//ucln
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")
#c
def rut_gon(tu, mau):
    if mau == 0:
        return "Mẫu số phải khác 0"
    common = math.gcd(tu, mau)
    tu_moi = tu // common
    mau_moi = mau // common
    return tu_moi, mau_moi
t_so = int(input("Nhập tử số: "))
m_so = int(input("Nhập mẫu số: "))
kq = rut_gon(t_so, m_so)
print(f"Phân số sau khi rút gọn là:{kq[0]}/{kq[1]}")
#d
def tim_max_min(n1, n2, n3):
    so_lon_nhat = max(n1, n2, n3)
    so_nho_nhat = min(n1, n2, n3)
    return so_lon_nhat, so_nho_nhat
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))
lon, nho = tim_max_min(x, y, z)
print(f"Số lớn nhất là:{lon}")
print(f"số nhỏ nhất là: {nho}")