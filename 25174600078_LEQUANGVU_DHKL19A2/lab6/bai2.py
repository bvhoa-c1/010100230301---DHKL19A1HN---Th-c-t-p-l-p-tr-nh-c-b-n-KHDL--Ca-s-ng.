import math

def la_so_nguyen_to(so):
    if so < 2:
        return False

    for i in range(2, int(math.sqrt(so)) + 1):
        if so % i == 0:
            return False

    return True

def la_so_hoan_hao(so):
    tong_uoc = 0

    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i

    return tong_uoc == so

so_luong = int(input("Nhap n: "))
danh_sach = []

for i in range(so_luong):
    so = int(input("Nhap so: "))
    danh_sach.append(so)

print("Cac so nguyen to:")
for so in danh_sach:
    if la_so_nguyen_to(so):
        print(so, end=" ")

print("\nCac so hoan hao:")
for so in danh_sach:
    if la_so_hoan_hao(so):
        print(so, end=" ")