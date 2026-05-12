kho_hang = {"apple", "banana", "orange", "grape", "mango", "pear", "melon"}
print("Danh mục kho hàng:", kho_hang)

nhap = input("Nhập các mặt hàng khách hàng đã chọn (cách nhau dấu phẩy): ")
da_chon = {item.strip() for item in nhap.split(",")}

# Phép toán tập hợp
chua_chon  = kho_hang - da_chon        # có trong kho nhưng chưa được chọn
co_trong_ca_hai = kho_hang & da_chon   # giao nhau

print("\nMặt hàng khách đã chọn (có trong kho):", co_trong_ca_hai)
print("Mặt hàng chưa được chọn mua          :", chua_chon)