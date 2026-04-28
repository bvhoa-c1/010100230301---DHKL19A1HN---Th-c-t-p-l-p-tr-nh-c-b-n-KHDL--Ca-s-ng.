def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

# a) Tìm UCLN của 2 số
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("UCLN của", a, "và", b, "là:", ucln(a, b))

# b) Tìm BCNN của 2 số
bcnn = abs(a * b) // ucln(a, b)
print("BCNN của", a, "và", b, "là:", bcnn)

# c) Rút gọn phân số
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

k = ucln(tu, mau)
tu_rg = tu // k
mau_rg = mau // k

print("Phân số sau khi rút gọn là:", tu_rg, "/", mau_rg)

# d) Tìm số nhỏ nhất và lớn nhất trong 3 số
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

so_nho_nhat = min(x, y, z)
so_lon_nhat = max(x, y, z)

print("Số nhỏ nhất là:", so_nho_nhat)
print("Số lớn nhất là:", so_lon_nhat)