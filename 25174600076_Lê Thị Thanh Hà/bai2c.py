def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(tu, mau):
    u = ucln(tu, mau)
    return tu // u, mau // u

# Test
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

tu_rg, mau_rg = rut_gon(tu, mau)
print("Phân số rút gọn:", f"{tu_rg}/{mau_rg}")