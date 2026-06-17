# Quản lý số lượng tồn kho và đơn giá bằng từ điển

kho_hang = {}

n = int(input("Nhap so luong mat hang: "))

for i in range(n):
    ten_hang = input("Nhap ten mat hang: ")
    so_luong = int(input("Nhap so luong ton kho: "))
    don_gia = int(input("Nhap don gia: "))

    kho_hang[ten_hang] = {
        "so_luong": so_luong,
        "don_gia": don_gia
    }

tong_chi_phi = 0

print("\n===== HOA DON CHI TIET =====")

for ten_hang, thong_tin in kho_hang.items():
    so_luong = thong_tin["so_luong"]
    don_gia = thong_tin["don_gia"]

    thanh_tien = so_luong * don_gia
    tong_chi_phi += thanh_tien

    print("Mat hang:", ten_hang)
    print("So luong:", so_luong)
    print("Don gia:", don_gia)
    print("Thanh tien:", thanh_tien)
    print("-------------------")

print("Tong chi phi:", tong_chi_phi)