# Bài 7.6 + 7.7 gộp lại để có dữ liệu đầy đủ

# -------------------- Bài 7.6 --------------------
# Khởi tạo từ điển quản lý hành trang
inventory = {
    'gold': 500,
    'backpack': ['xà beng', 'súng', 'băng gạc', 'dao', 'đèn pin']
}

print("=== TRƯỚC KHI XỬ LÝ ===")
print("Túi đồ (backpack):", inventory['backpack'])
print("Vàng:", inventory['gold'])

# Bổ sung khóa 'pocket' với danh sách vật phẩm
inventory['pocket'] = ['đá lửa', 'dây thừng', 'la bàn']
print("\n=== SAU KHI THÊM POCKET ===")
print("Túi hông (pocket):", inventory['pocket'])

# Cập nhật số lượng vàng
inventory['gold'] += 50
print("Vàng sau khi cập nhật:", inventory['gold'])

# -------------------- Bài 7.7 --------------------
# Sắp xếp danh sách vật phẩm trong backpack theo thứ tự từ điển
print("\n=== TRƯỚC KHI SẮP XẾP ===")
print("Backpack (chưa sắp xếp):", inventory['backpack'])

# Sắp xếp (dùng thuật toán nổi bọt đơn giản cho sinh viên năm nhất)
backpack_list = inventory['backpack']
n = len(backpack_list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if backpack_list[j] > backpack_list[j + 1]:
            # Đổi chỗ
            backpack_list[j], backpack_list[j + 1] = backpack_list[j + 1], backpack_list[j]

print("Backpack (sau khi sắp xếp):", inventory['backpack'])

# Loại bỏ một vật phẩm cụ thể
item_to_remove = 'súng'
if item_to_remove in inventory['backpack']:
    inventory['backpack'].remove(item_to_remove)
    print(f"\nĐã loại bỏ '{item_to_remove}' khỏi backpack")
else:
    print(f"\nKhông tìm thấy '{item_to_remove}' trong backpack")

# In kết quả cuối cùng
print("\n=== KẾT QUẢ CUỐI CÙNG ===")
print("Từ điển inventory:", inventory)
print("Backpack sau khi xử lý:", inventory['backpack'])
print("Pocket:", inventory['pocket'])
print("Vàng:", inventory['gold'])