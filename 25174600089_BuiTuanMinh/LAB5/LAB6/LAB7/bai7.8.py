ton_kho   = {"apple": 100, "banana": 50, "orange": 75, "grape": 30}
don_gia   = {"apple": 5000, "banana": 3000, "orange": 7000, "grape": 12000}

print("Danh sách mặt hàng:", list(ton_kho.keys()))

so_mat_hang = int(input("Số mặt hàng muốn mua: "))

don_hang = {}
for _ in range(so_mat_hang):
    ten = input("  Tên mặt hàng: ").strip()
    sl  = int(input(f"  Số lượng {ten}: "))
    if ten in ton_kho and ton_kho[ten] >= sl:
        don_hang[ten] = sl
    else:
        print(f"  '{ten}' không đủ hàng hoặc không tồn tại!")

# In hóa đơn
print("             HÓA ĐƠN MUA HÀNG")
print(f"{'Mặt hàng':<12} {'SL':>4}  {'Đơn giá':>10}  {'Thành tiền':>12}")

tong = 0
for ten, sl in don_hang.items():
    gia = don_gia[ten]
    thanh_tien = gia * sl
    tong += thanh_tien
    print(f"{ten:<12} {sl:>4}  {gia:>10,}  {thanh_tien:>12,}")
print(f"{'TỔNG CỘNG':>32}  {tong:>12,} VNĐ")
