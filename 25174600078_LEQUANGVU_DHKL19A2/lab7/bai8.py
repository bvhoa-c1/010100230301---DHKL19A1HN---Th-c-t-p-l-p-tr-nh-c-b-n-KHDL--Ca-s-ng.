so_luong = {
    "but": 10,
    "sua": 5,
    "banh": 8
}

don_gia = {
    "but": 5000,
    "sua": 30000,
    "banh": 12000
}

tong_tien = 0

print("HOA DON")

for mat_hang in so_luong:
    thanh_tien = so_luong[mat_hang] * don_gia[mat_hang]
    tong_tien += thanh_tien

    print(mat_hang, "-", so_luong[mat_hang], "-", thanh_tien)

print("Tong tien:", tong_tien)