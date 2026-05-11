so_luong = int(input("Nhap n: "))
danh_sach = []

for i in range(so_luong):
    so = int(input(f"Nhap phan tu thu {i + 1}: "))
    danh_sach.append(so)

tong_chan = 0
tong_le = 0

for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

print("Tong cac so chan:", tong_chan)
print("Tong cac so le:", tong_le)