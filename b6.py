def ucln(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // ucln(a, b)


def rut_gon_phan_so(tu, mau):
    if mau == 0:
        return None
    if mau < 0:
        tu, mau = -tu, -mau
    g = ucln(tu, mau)
    return tu // g, mau // g


def min_max_3(a, b, c):
    return min(a, b, c), max(a, b, c)


try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    print(f"UCLN({a}, {b}) = {ucln(a, b)}")
    print(f"BCNN({a}, {b}) = {bcnn(a, b)}")

    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    phan_so = rut_gon_phan_so(tu, mau)
    if phan_so is None:
        print("Mẫu số không hợp lệ (không được bằng 0).")
    else:
        tu_rg, mau_rg = phan_so
        print(f"Phân số rút gọn: {tu_rg}/{mau_rg}")

    x = int(input("Nhập số nguyên thứ nhất: "))
    y = int(input("Nhập số nguyên thứ hai: "))
    z = int(input("Nhập số nguyên thứ ba: "))
    nho_nhat, lon_nhat = min_max_3(x, y, z)
    print(f"Số nhỏ nhất: {nho_nhat}")
    print(f"Số lớn nhất: {lon_nhat}")
except ValueError:
    print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")