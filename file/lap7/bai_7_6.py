# Bài 7.6: Quản lý hành trang (Inventory) - thêm khóa và cập nhật

# Khởi tạo từ điển hành trang
inventory = {
    'backpack': ['sword', 'shield', 'potion'],
    'gold': 100
}

print("Trạng thái hành trang ban đầu:")
print(inventory)

# Bổ sung trường dữ liệu mới (khóa pocket)
inventory['pocket'] = ['coin', 'key', 'map']

print("\nSau khi thêm pocket:")
print(inventory)

# Cập nhật số lượng cho khóa gold
inventory['gold'] += 50

print("\nSau khi cập nhật gold:")
print(inventory)

# In chi tiết từ điển
print("\nChi tiết hành trang:")
for key, value in inventory.items():
    print(f"  {key}: {value}")
