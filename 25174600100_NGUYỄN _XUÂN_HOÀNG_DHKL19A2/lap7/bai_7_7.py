# Bài 7.7: Sắp xếp backpack và loại bỏ vật phẩm

inventory = {
    'backpack': ['sword', 'shield', 'potion', 'apple', 'book'],
    'pocket': ['coin', 'key', 'map'],
    'gold': 150
}

print("Hành trang ban đầu:")
print(f"Backpack: {inventory['backpack']}")

# Sắp xếp theo thứ tự từ điển
inventory['backpack'].sort()

print("\nSau khi sắp xếp từ điển:")
print(f"Backpack: {inventory['backpack']}")

# Loại bỏ một vật phẩm cụ thể
item_to_remove = input("\nNhập tên vật phẩm muốn loại bỏ: ")

if item_to_remove in inventory['backpack']:
    inventory['backpack'].remove(item_to_remove)
    print(f"Đã loại bỏ '{item_to_remove}' khỏi backpack")
else:
    print(f"Không tìm thấy '{item_to_remove}' trong backpack")

print(f"\nBackpack sau khi loại bỏ:")
print(f"Backpack: {inventory['backpack']}")
