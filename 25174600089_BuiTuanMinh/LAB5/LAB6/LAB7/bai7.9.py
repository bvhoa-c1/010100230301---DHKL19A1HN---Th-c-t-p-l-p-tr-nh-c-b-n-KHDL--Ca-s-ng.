ton_kho = {"apple": 100, "banana": 50, "orange": 75, "grape": 30}

print("Tồn kho ban đầu:")
for ten, sl in ton_kho.items():
    print(f"  {ten}: {sl}")

so_giao_dich = int(input("\nNhập số giao dịch: "))

for _ in range(so_giao_dich):
    ten = input("  Tên mặt hàng: ").strip()
    sl  = int(input(f"  Số lượng giao dịch {ten}: "))

    if ten not in ton_kho:
        print(f"   Mặt hàng '{ten}' không tồn tại!")
    elif ton_kho[ten] < sl:
        print(f"   Không đủ hàng! Hiện có: {ton_kho[ten]}")
    else:
        ton_kho[ten] -= sl
        print(f"   Giao dịch thành công. Còn lại: {ton_kho[ten]}")

print("\nBáo cáo tồn kho hiện tại:")
for ten, sl in ton_kho.items():
    trang_thai = "⚠ Sắp hết" if sl < 20 else "Đủ hàng"
    print(f"  {ten:<10}: {sl:>4}  [{trang_thai}]")