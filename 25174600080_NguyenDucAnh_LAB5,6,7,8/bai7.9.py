# Thực hiện thủ tục khấu trừ số lượng vật phẩm đã giao dịch thành công

# Khởi tạo kho hàng
kho_hang = {}

n = int(input("Nhap so luong mat hang: "))

for i in range(n):
    ten_hang = input("Nhap ten mat hang: ")
    so_luong = int(input("Nhap so luong ton kho: "))

    kho_hang[ten_hang] = so_luong

# Thực hiện giao dịch
ten_giao_dich = input("Nhap ten mat hang can mua: ")
so_luong_mua = int(input("Nhap so luong can mua: "))

# Kiểm tra và khấu trừ
if ten_giao_dich in kho_hang:
    if kho_hang[ten_giao_dich] >= so_luong_mua:
        kho_hang[ten_giao_dich] -= so_luong_mua
        print("Giao dich thanh cong")
    else:
        print("Khong du hang trong kho")
else:
    print("Mat hang khong ton tai")

# Xuất báo cáo tồn kho
print("\n===== TON KHO SAU GIAO DICH =====")

for ten_hang, so_luong in kho_hang.items():
    print(ten_hang, ":", so_luong)